from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.markers import MarkerStyle
import matplotlib
import analysis

matplotlib.use("TkAgg")

# from utils import analysis, plot, utils
# from data_processing import load_dict, fingers, finger_labels

# def plot_hit_curves(experiment, subjects, subjects_to_plot=[], ax=None):
#     stats = []
#     hf = []
#     if ax is None:
#         fig, ax = plt.subplots(1, 1, figsize=(24, 8))
#     for subject in subjects:
#         hits, misses, noholds, num_sessions = get_outcomes(experiment, subject)
#         fractions = [h * (100 / 12) for h in hits]
#         sessions_idxs = range(len(fractions))
#         # x = np.linspace(0, num_sessions, 50)
#         # popt, pcov = curve_fit(log, list(range(1, num_sessions + 1)), fractions)
#         total_fraction = 100 * sum(hits) / (num_sessions * 12)
#         # rate = popt[1]
#         stats.append(
#             f"{subject}: \n Hit Fraction: {round(total_fraction,1)}% \n"
#         )  # \n Baseline: {round(popt[0],1)}% \n Rate: {round(rate,1)} \n")
#         hf.append(total_fraction)
#         if subject in subjects_to_plot:
#             ax.plot(fractions, "-o", label=subject, zorder=10)
#             # plt.plot(x, log(x, *popt), "k--", zorder=10)
#         else:
#             ax.plot(fractions, "-o", color="gray", alpha=0.3)
#             # plt.plot(x, log(x, *popt), "k--", alpha=0.3)
#     ax.set_xlabel("block")
#     ax.set_ylabel("hit fraction")
#     ax.set_title("hit fractions over sessions")
#     ax.set_ylim([0, 100])
#     ax.set_xticks(range(num_sessions))
#     ax.set_xticklabels(range(1, num_sessions + 1))
#     ax.grid(True, which="major")
#     ax.legend()
#     return ax, hf, stats


def save_figure(fig, name, folder="."):
    # if folder doesn't exist, make it
    if folder != ".":
        Path(folder).mkdir(exist_ok=True, parents=True)
        savepath = Path(folder) / Path(name + ".pdf")
    else:
        savepath = Path(name + "pdf")
    fig.savefig(
        savepath,
        pad_inches=0.1,
        bbox_inches="tight",
        dpi=300,
        format="pdf",
        transparent=False,
    )


def plot_circle(x, y, r, ax, style="k"):
    theta = np.linspace(0, 2 * np.pi, 100)
    ax.plot(r * np.cos(theta) + x, r * np.sin(theta) + y, style)


def plot_targets(ax, style="ko", markersize=5, target=None):
    m = MarkerStyle("o", fillstyle="none")
    theta = (np.linspace(0, 2 * np.pi, 13) + np.pi)[:-1]
    ax.plot(
        np.cos(theta),
        np.sin(theta),
        style,
        marker=m,
        markersize=markersize,
        color="grey",
    )
    if not target is None:
        ax.plot(target[0], target[1], "ro", markersize=markersize)


def plot_box(ax):
    ax.plot(0, 0, "ks", zorder=20)
    plot_circle(0, 0, 0.15, ax)
    ax.plot([-1, 1], [-1, -1], "k")
    ax.plot([-1, 1], [1, 1], "k")
    ax.plot([1, 1], [-1, 1], "k")
    ax.plot([-1, -1], [-1, 1], "k")


def plot_preprocessing_steps(signal, ax=None):
    if ax is None:
        fig, ax = plt.subplots(1, 1, figsize=(12, 10))
    # 1D signal
    ax.plot(analysis.rectify(signal), label="R")
    ax.plot(analysis.rectify(analysis.highpass(signal, cutoff=55)), label="HP + R")
    pp = analysis.lowpass(
        analysis.rectify(analysis.highpass(signal, cutoff=60)), cutoff=3
    )
    ax.plot(pp, label="HP + R + LP", linewidth=2, color="purple")
    ax.plot(pp - pp.mean(), label="HP + R + LP + MS", linewidth=2, color="green")
    ax.legend()
    ax.set_xlabel("sample")
    ax.set_ylabel("EMG activation [AU]")
    return fig, ax


# def plot_psd(data, freq=2000, legend=False, fig=None):
#     dim = len(data.shape)
#     if fig is None:
#         fig, ax = plt.subplots(1, 1)

#     if dim == 2:
#         for i, channel in enumerate(data):
#             ax.psd(channel,
#                    Fs=freq,
#                    detrend='linear',
#                    label="Channel " + str(i))
#             if legend:
#                 plt.legend()
#     elif dim == 1:
#         plt.figure()
#         ax.psd(data, Fs=freq, detrend='linear', label='PSD')
#     else:
#         raise ValueError("data array must be 1D or 2D")
#     # line = mlines.Line2D([50, 50], [-100, -50])
#     # line.set_color('red')
#     # line.set_linestyle('--')
#     # ax.add_line(line)
#     return fig, ax


# def plot_trajectories(a,
#                       freq=2000,
#                       nticks=20,
#                       sep=0,
#                       show_yticks=True,
#                       ylabel=None):
#     fig, ax = plt.subplots(1, 1, figsize=(10, 8))
#     assert a.shape[0] < a.shape[1]
#     num_t = a.shape[0]
#     cvec = plot.make_color_vector("viridis", num_t + 3)
#     offset = 0
#     for i in range(num_t):
#         ax.plot(a[i, :] + offset, color=cvec[i])
#         offset += sep
#     ax.set_xlabel("Time [s]")
#     ticks = np.linspace(0, a.shape[1], nticks)
#     ticklabels = [
#         str(np.round(i, 1)) for i in np.linspace(0, a.shape[1] / freq, nticks)
#     ]
#     ax.set_xticks(ticks)
#     ax.set_xticklabels(ticklabels)
#     if ylabel is not None:
#         ax.set_ylabel(ylabel)
#     if not show_yticks:
#         ax.set_yticks([])
#     else:
#         if sep != 0:
#             ax.set_yticks(np.linspace(0, num_t * sep, num_t))
#             ax.set_yticklabels(np.linspace(1, num_t, num_t, dtype=np.int))
#     return fig, ax


# def plot_features(features, ax, title, vmin=0, vmax=1):
#     ax.set_xticks([])
#     yt = np.arange(0, 32, 3)
#     ax.set_yticks(yt)
#     ax.set_xticklabels(yt + 1)
#     ax.set_frame_on(0)
#     ax.set_title(title)
#     ax.imshow(features, vmin=vmin, vmax=vmax, origin="lower")
#     return fig, ax


# def plot_PCA_variances():
#     PCA_variance_dict = load_dict("finger_PCA_variances")
#     fig = plt.figure(figsize=(9, 10), constrained_layout=True)
#     spec = fig.add_gridspec(ncols=2, nrows=len(fingers) // 2)
#     num_comps_to_plot = 5
#     # number of trials per plot
#     colors = plot.make_color_vector("viridis",
#                                     PCA_variance_dict[fingers[0]].shape[0])
#     x = np.arange(1, num_comps_to_plot + 1)
#     for row, finger, finger_label in zip(range(len(fingers)), fingers,
#                                          finger_labels):
#         if row > 3:
#             row -= 4
#             col = 1
#         else:
#             col = 0
#         ax = fig.add_subplot(spec[row, col])
#         ax.set_xticks(x)
#         ax.set_yticks(np.linspace(0, 1, 3))
#         ax.set_ylim([0, 1])
#         ax.set_title(finger_label.strip("\n"))
#         ax.errorbar(x,
#                     np.mean(PCA_variance_dict[finger][:, :num_comps_to_plot],
#                             axis=0),
#                     yerr=np.std(
#                         PCA_variance_dict[finger][:, :num_comps_to_plot],
#                         axis=0),
#                     fmt="or",
#                     zorder=100,
#                     capsize=2,
#                     label="mean")
#         # # for each trial's variance vector
#         for i, v in enumerate(
#                 PCA_variance_dict[finger][:, :num_comps_to_plot]):
#             if i == num_comps_to_plot - 1:
#                 ax.plot(x,
#                         v,
#                         "o",
#                         color="k",
#                         alpha=0.5,
#                         zorder=1,
#                         label="trial")
#             else:
#                 ax.plot(x, v, "o", color="k", alpha=0.5, zorder=1)
#         if row == 3 and col == 0:
#             ax.set_xlabel("PCA component")
#             ax.set_ylabel("variance\ncaptured")
#             ax.legend(loc="upper right")
#     # fig.suptitle("PCA Component Variances")
#     return fig, ax


# def plot_PCA_components():
#     PCA_feature_dict = load_dict("finger_PCA_features")
#     fig = plt.figure(figsize=(9, 10))  #, constrained_layout=True)
#     spec = fig.add_gridspec(ncols=3, nrows=4, width_ratios=[20, 20, 1])
#     vmin = 0
#     vmax = 1
#     for i, finger in enumerate(fingers):
#         if i > 3:
#             row = i - 4
#             col = 1
#         else:
#             row = i
#             col = 0
#         ax = fig.add_subplot(spec[row, col])
#         plot_features(PCA_feature_dict[finger],
#                       ax,
#                       vmin=vmin,
#                       vmax=vmax,
#                       title=finger_labels[i].strip("\n"))
#         ax.set_yticks([i - 0.5 for i in range(3, 15, 3)], minor=True)
#         ax.yaxis.grid(True, which='minor')
#         ax.yaxis.grid(False, which='major')
#         ax.xaxis.grid(False)
#         ax.set_yticklabels(np.arange(1, 15, 3))
#         if row == 3:
#             ax.set_xlabel("channel")
#             ax.set_xticks([0, 15, 31])
#             ax.set_xticklabels([1, 16, 32])
#             ax.set_ylabel("trial")
#         if col == 0:
#             ax.set_ylabel("trial")
#     cbax = fig.add_subplot(spec[1:3, -1])
#     cmap = matplotlib.cm.get_cmap('viridis')
#     norm = matplotlib.colors.Normalize(vmin=vmin, vmax=vmax)
#     matplotlib.colorbar.ColorbarBase(cbax,
#                                      cmap=cmap,
#                                      norm=norm,
#                                      orientation='vertical')
#     cbax.set_ylabel('weight')
#     return fig, ax


# def plot_task_trajectories():
#     colors = plot.make_color_vector("viridis", 3)
#     fig = plt.figure(figsize=(18, 6))  #, constrained_layout=True)
#     spec = fig.add_gridspec(ncols=3, nrows=2, height_ratios=[20, 1])
#     colors = plot.make_color_vector("viridis", 32)
#     targets = utils.roots_of_unity(32)
#     for block in blocks:
#         ax = fig.add_subplot(spec[0, block - 1])
#         block_dict = center_hold_dict[block]["trials"]
#         trial_nos = []
#         dropped_frames = []
#         for trial_no, trial_dict in sorted(block_dict.items()):
#             trial_nos.append(trial_no)
#             trial_df = trial_dict["task"]["data"]
#             direction = trial_dict["direction"]
#             trial_df.columns = ["Frame", "Timestamp", "X", "Y"]
#             trial_array = trial_df.to_numpy()
#             # num_frames = int(np.max(trial_array[:, 0])) + 1
#             # trajectory = np.empty((num_frames, 2))
#             # for i in range(num_frames):
#             # find the last value before the frame switches
#             # ended up not using this because it looks glitchy
#             # it must be glitchy in bonsai as well...
#             # can we trigger dynamics on frames?
#             # for now just plot everything
#             # last_frame_indices = np.where(trial_array[:, 0] == i)[0]
#             # if len(last_frame_indices) == 0:
#             # dropped_frames.append(i)
#             # continue
#             # else:
#             # frame_idx = last_frame_indices[0]
#             # trajectory[i, :] = trial_array[frame_idx, -2:]
#             ax.plot(trial_array[:, -2],
#                     trial_array[:, -1],
#                     color=colors[direction])
#             # plot targets
#         print(f"dropped {len(dropped_frames)} frames in block {block}")
#         for ti, t in enumerate(targets):
#             ax.scatter(t[0],
#                        t[1],
#                        marker="o",
#                        color=colors[ti],
#                        s=25,
#                        edgecolor="r",
#                        zorder=100)
#         ax.set_aspect("equal")
#         ax.set_title(f"block {block}")
#         if block == 3:
#             ax.set_xlabel("$x$ position")
#         ax.set_ylabel("$y$ position")
#         ax.set_xlim([-2, 2])
#         ax.set_ylim([-2, 2])
#     cbax = fig.add_subplot(spec[1, 1])
#     cmap = matplotlib.cm.get_cmap('viridis')
#     norm = matplotlib.colors.Normalize(vmin=1, vmax=len(colors))
#     matplotlib.colorbar.ColorbarBase(cbax,
#                                      cmap=cmap,
#                                      norm=norm,
#                                      orientation='horizontal')
#     cbax.set_xlabel('target direction')
#     return fig, ax


# # look at behavior array
# def plot_hit_fractions():
#     block = 1
#     num_hits = []
#     num_hold_timeouts = []
#     num_reach_timeouts = []
#     num_trials = []
#     for block in blocks:
#         behavior_df = center_hold_dict[block]["behavior"]["data"]
#         behavior_array = behavior_df.to_numpy()
#         outcomes = behavior_df["Outcome"]
#         num_hits.append(len(np.where(outcomes == 1)[0]))
#         num_hold_timeouts.append(len(np.where(outcomes == 0)[0]))
#         num_reach_timeouts.append(len(np.where(outcomes == -1)[0]))
#         num_trials.append(behavior_array[:, 0].shape[0])
#     hit_fractions = [nh / nt for nh, nt in zip(num_hits, num_trials)]
#     hold_timeout_fractions = [
#         nh / nt for nh, nt in zip(num_hold_timeouts, num_trials)
#     ]
#     reach_timeout_fractions = [
#         nh / nt for nh, nt in zip(num_reach_timeouts, num_trials)
#     ]

#     fig, ax = plt.subplots(1, 1)
#     barwidth = 0.4
#     ax.bar(
#         blocks,
#         hit_fractions,
#         bottom=[
#             rt + ht
#             for rt, ht in zip(reach_timeout_fractions, hold_timeout_fractions)
#         ],
#         width=barwidth,
#         label="hit fraction")
#     ax.bar(blocks,
#            reach_timeout_fractions,
#            bottom=hold_timeout_fractions,
#            width=barwidth,
#            label="reach timeout fraction")
#     ax.bar(blocks,
#            hold_timeout_fractions,
#            width=barwidth,
#            label="hold timeout fraction")
#     ax.legend(loc='center', bbox_to_anchor=(1.2, 0.5))
#     ax.set_xticks(blocks)
#     ax.set_xticklabels(blocks)
#     yticks = np.round(np.linspace(0, 1, 11), decimals=1)
#     ax.set_yticks(yticks)
#     ax.set_yticklabels(yticks)
#     ax.set_xlabel("block")
#     ax.set_ylabel("fraction")
#     fig.tight_layout()
#     return fig, ax


# # PCA on trajectories
# # average PCA variance per block over components
# def plot_task_PCA_variances():
#     center_hold_PCA_variance_dict = load_dict("task_PCA_variance")
#     fig, ax = plt.subplots(1, 1, figsize=(9, 9))
#     num_comps_to_plot = 5
#     # number of trials per plot
#     colors = plot.make_color_vector("viridis", len(blocks) * 2)
#     x = np.arange(1, num_comps_to_plot + 1)
#     for block in blocks:
#         variances = []
#         for trial_no, variance in sorted(
#                 center_hold_PCA_variance_dict[block].items()):
#             offset = block * 0.1
#             ax.plot(x + offset,
#                     variance[:num_comps_to_plot],
#                     "o",
#                     color=colors[block],
#                     alpha=0.1,
#                     zorder=1)
#             variances.append(variance[:num_comps_to_plot])
#         variances = np.array(variances)
#         ax.errorbar(x + offset,
#                     np.mean(variances, axis=0),
#                     label="block " + str(block),
#                     yerr=np.std(variances, axis=0),
#                     fmt="o",
#                     color=colors[block],
#                     capsize=5,
#                     zorder=100)

#     ax.set_xlabel("PCA component")
#     ax.set_ylabel("variance captured")
#     ax.legend()
#     ax.set_xticks(x)
#     ax.set_yticks(np.round(np.linspace(0, 1, 15), decimals=2))
#     ax.set_ylim([0, 1])
#     return fig, ax


# def plot_task_concat_PCA_variances():
#     center_hold_PCA_variance_dict = load_dict("task_concat_PCA_variance")
#     fig, ax = plt.subplots(1, 1, figsize=(9, 9))
#     num_comps_to_plot = 5
#     # number of trials per plot
#     colors = plot.make_color_vector("viridis", len(blocks) * 2)
#     x = np.arange(1, num_comps_to_plot + 1)
#     for block in blocks:
#         offset = block * 0.1
#         ax.scatter(x + offset,
#                    center_hold_PCA_variance_dict[block][:num_comps_to_plot],
#                    label="block " + str(block),
#                    color=colors[block],
#                    zorder=100)
#     ax.set_xlabel("PCA component")
#     ax.set_ylabel("variance captured")
#     ax.legend()
#     ax.set_xticks(x)
#     ax.set_yticks(np.round(np.linspace(0, 1, 15), decimals=2))
#     ax.set_ylim([0, 1])
#     return fig, ax


# def plot_distance_matrix():
#  plot distance between each PCA component in a distance matrix
# feature_stack = np.vstack(
#     [feature_dict[finger][:, 0, :] for finger in fingers])
# fig, ax = plt.subplots(1, 1, figsize=(12, 12))
# ax.imshow(distance_matrix(feature_stack))
# ax.set_xticks(np.arange(0, 120, 30)[1:] - 0.5, minor=True)
# ax.set_yticks(np.arange(0, 120, 30)[1:] - 0.5, minor=True)
# ax.yaxis.grid(True, which='minor', color="w")
# ax.xaxis.grid(True, which='minor', color="w")


# if __name__ == '__main__':

#     images_folder = "/Users/spencerw/Google Drive/motor_control/phd/images/"
#     finger = "ring_flex"
#     trial = 2
#     channel = 11
#     blocks = [1, 2, 3]
#     num_bio_channels = 32

#     ## ## finger trials
#     finger_data_folder = images_folder + "data_analysis/fingers/"

#     raw_data_dict = load_dict("finger_data")
#     trajectory_dict = load_dict("finger_trajectories")

#     fig, ax = plot_trajectories(
#         raw_data_dict[finger][trial][:num_bio_channels],
#         sep=150,
#         show_yticks=True,
#         ylabel="EMG Channels")
#     save_figure(fig, "raw_data", folder=finger_data_folder)

#     fig, ax = plot_psd(raw_data_dict[finger][trial][:32])
#     save_figure(fig, "psd", folder=finger_data_folder)

#     fig, ax = plot_preprocessing_steps(raw_data_dict[finger][trial][channel])
#     save_figure(fig, "preprocessing_steps", folder=finger_data_folder)

#     fig, ax = plot_trajectories(trajectory_dict[finger][trial],
#                                 ylabel="EMG Activation [AU]")
#     save_figure(fig, "preprocessed_data", folder=finger_data_folder)

#     fig, ax = plot_PCA_variances()
#     save_figure(fig, "PCA_variances", folder=finger_data_folder)

#     fig, ax = plot_PCA_components()
#     save_figure(fig, "PCA_components", folder=finger_data_folder)

#     ## ## center hold task
#     center_hold_dict = load_dict("center_hold_12_9")
#     center_hold_folder = images_folder + "data_analysis/center_hold/"
#     fig, ax = plot_hit_fractions()
#     save_figure(fig, "hit_fraction", folder=center_hold_folder)
#     fig, ax = plot_task_trajectories()
#     save_figure(fig, "trajectories", folder=center_hold_folder)
#     fig, ax = plot_task_PCA_variances()
#     save_figure(fig, "PCA_trial_variance", folder=center_hold_folder)
#     fig, ax = plot_task_concat_PCA_variances()
#     save_figure(fig, "PCA_concat_variance", folder=center_hold_folder)
#     # plt.show()
