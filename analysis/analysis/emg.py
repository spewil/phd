import sys
import numpy as np
import scipy.signal
import scipy.ndimage









def make_kernel(kernel_length, cutoff_hz, sample_rate_hz, mode="lowpass"):
    """
        filter delay is (window - 1)/(2 * sample_rate)
        (((1000 - 1) / 2) samples) / 2000 samples/sec 

        Output delay is the amount of time it takes for a change 
        on the input to fully reflect on the output. It can also be
        expressed in samples and is equal to filter order 
        (window-1). 

        To be precise the group delay of a linear phase FIR filter is (𝑁−1)/2 samples, where 𝑁 is 
        the filter length (i.e. the number of taps). The group delay is constant for all 
        frequencies, because the filter has a linear phase, i.e. its impulse response is symmetrical 
        (or asymmetric). A linear phase means that all frequency components of the input signal 
        experience the same delay, i.e. there are no phase distortions. So for a frequency selective 
        filter (e.g., a low pass filter), if the input signal is in the passband of the filter, the 
        output signal is approximately equal to the input signal delayed by the group delay of the 
        filter. Note that in general FIR filters do not have a linear phase response. In this case, 
        the group delay is a function of frequency.
        https://dsp.stackexchange.com/questions/18435/group-delay-of-the-fir-filter 

        Group delay is the time lag of the amplitude envelopes of 
        the various sinusoidal components of the input signal through 
        the filter. It can also be expressed in samples and is 
        equal to half the filter order ((window-1)/2). 

    """
    # based on https://github.com/bonsai-rx/bonsai/blob/9c4db22dfa43a7b20fb8de7cb4eb079b19cfa027/Bonsai.Dsp/FrequencyFilter.cs#L153
    # Low-pass windowed-sinc filter: http://www.dspguide.com/ch16/4.htm
    cutoffRadians = 2 * np.pi * cutoff_hz / sample_rate_hz
    kernel = np.zeros((kernel_length + 1, 1))
    for i in range(kernel_length):
        normalizer = i - (kernel_length // 2)
        if normalizer == 0:
            kernel[i] = cutoffRadians
        else:
            kernel[i] = np.sin(cutoffRadians * normalizer) / normalizer

        # Blackman window: http://www.dspguide.com/ch16/1.htm
        kernel[i] = kernel[i] * (
            0.42
            - 0.5 * np.cos(2 * np.pi * i / kernel_length)
            + 0.08 * np.cos(4 * np.pi * i / kernel_length)
        )

    # Normalize for unit gain
    sum = np.sum(kernel)
    kernel /= sum

    if mode == "highpass":
        kernel *= -1
        # add unit impulse to the center of the kernel
        # in freq domain:
        # k_hp(f) = 1 - k_lp(f)
        kernel[(kernel.shape[0]) // 2] += 1

    return kernel[:-1]


def highpass(a, kernel=None):
    if kernel is None:
        kernel = make_kernel(250, 0.1, 2000, mode="highpass")
    # cut off the end where it's extended for the "full" convolution
    return scipy.signal.convolve2d(a, kernel, mode="full", boundary="symm",)[
        : -kernel.shape[0] + 2
    ]


def standardize(a, var):
    return (var @ a.T).T


def rectify(a):
    return np.abs(a)


def lowpass(a, kernel=None):
    if kernel is None:
        kernel = make_kernel(750, 5.0, 2000, mode="lowpass")
    return scipy.signal.convolve2d(a, kernel, mode="full", boundary="symm")[
        : -kernel.shape[0] + 2
    ]


def subsample(a):
    return a[::10, :]

def fast_lowpass(a, kernel=None):
    if kernel is None:
        kernel = make_kernel(750, 5.0, 2000, mode="lowpass")
    return scipy.signal.fftconvolve(a, kernel, mode="valid",axes=(0))

def fast_highpass(a, kernel=None):
    if kernel is None:
        kernel = make_kernel(250, 0.1, 2000, mode="highpass")
    return scipy.signal.fftconvolve(a, kernel, mode="valid",axes=(0))


def filter_emg(a, var, lowpass_kernel=None, highpass_kernel=None):
    assert a.shape[1] == 64
    # return subsample(lowpass(rectify(standardize(highpass(a,highpass_kernel), var)),lowpass_kernel))
    # changed the line above to what's below for speedup!
    # we need to refect the beginning of the signal to have a valid length
    # 1000 is the length of the two kernels combined
    reflected = np.concatenate([a[:1000][::-1], a],axis=0)
    return subsample(fast_lowpass(rectify(standardize(fast_highpass(reflected,highpass_kernel), var)),lowpass_kernel))

def offline_highpass(sig, cutoff=50):
    b, a = scipy.signal.butter(2, cutoff, "highpass", analog=False, fs=2000)
    return scipy.signal.filtfilt(b, a, sig, axis=0)


def offline_lowpass(sig, cutoff=500):
    b, a = scipy.signal.butter(2, cutoff, "lowpass", analog=False, fs=2000)
    return scipy.signal.filtfilt(b, a, sig, axis=0)


def offline_filter_emg(a, var):
    assert var.shape == (64,64)
    assert a.shape[0] > a.shape[1]
    filtered = rectify(offline_lowpass(rectify(standardize(offline_highpass(a, cutoff=5), var)), cutoff=5))
    return filtered








# THIS STUFF IS OLD, NOT EVEN SURE WHERE IT'S USED?

# def preprocess_emg(
#     recording, nch=68, start=200, end=-1, lowcutoff=5, highcutoff=60, mean=None
# ):
#     # highpass, rectify, lowpass, mean subtract per channel
#     data_subset = recording[:nch, :]
#     for channel, t in enumerate(data_subset):
#         data_subset[channel, :] = lowpass(
#             rectify(highpass(data_subset[channel, :], cutoff=highcutoff)),
#             cutoff=lowcutoff,
#         )
#     if mean is None:
#         out = data_subset - data_subset[:, start - 1 : end].mean(axis=1).reshape(-1, 1)
#     else:
#         out = data_subset - mean
#     return out[:, start - 1 : end]


# def get_axis():
#     return 0


# def notch(sig, freq=50):
#     """
#     Not really sure how to tune this effectively...
#     """
#     b, a = scipy.signal.iirnotch(freq, 30, fs=2000)
#     return scipy.signal.filtfilt(b, a, sig, axis=get_axis())


# def moving_average(a, window_length=100):
#     """
#     boxcar window average
#     """
#     return (
#         scipy.ndimage.convolve1d(a, np.ones((window_length)), axis=1, mode="nearest")
#         / window_length
#     )


# def blur(a, sigma=50):
#     """
#     gaussian convolution
#     """
#     return scipy.ndimage.gaussian_filter1d(a, sigma=sigma, axis=1, mode="nearest")


# def demean(a):
#     assert a.shape[0] < a.shape[1]
#     return a - np.mean(a, axis=1).reshape(-1, 1)


# def preprocess(data, sigma=40):
#     data_mv = data * 0.0002861
#     data_mv = demean(data_mv)
#     output = rectify(data_mv)
#     output = blur(output, sigma)
#     return output


# def get_dropped_samples(counter):
#     if len(counter.shape) > 1:
#         counter = counter[0]
#     drops = (counter[1:] - counter[:-1]) - 1
#     drops[np.where(drops == -(2**16))] = 0
#     for idx in np.where(drops != 0):
#         print(f"Dropped {drops[idx]} samples at {idx}")
#     return drops


# def fill_time_array(dataset):
#     dataset["time"] = np.arange(
#         0, len(dataset.time) / dataset.sampling_rate, 1 / dataset.sampling_rate
#     )
