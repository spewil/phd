import numpy as np
from pathlib import Path
import json
import sys
import pickle
import scipy as sp

if sys.platform == "linux":
    ROOT_RAWDATA_PATH = Path("/home/spencer/motor-control/data/rawdata/")
    ROOT_METADATA_PATH = Path("/home/spencer/motor-control/data/metadata/")  
else:   
    ROOT_RAWDATA_PATH = Path("/Users/spencer/motor-control/data/rawdata/")
    ROOT_METADATA_PATH = Path("/Users/spencer/motor-control/data/metadata/")

### Modeling

def linear_fit(x_data, y_data):
    result = sp.stats.linregress(x_data, y_data)
    return result

def linspace(data):
    return np.linspace(np.min(data),np.max(data),100,endpoint=True)

def cosine_distance(A,B):
    # insensitive to magnitude, "directional"
    return 1 - (np.trace(np.dot(A,B)) / (np.linalg.norm(A,ord='fro') * np.linalg.norm(B,ord='fro')))

def frobenius_difference(A,B):
    # sensitive to magnitudes
    return np.linalg.norm(A-B,ord='fro')



### FILES

def load_subjects():
    with open('olympics_subjects.pkl', 'rb') as handle:
        return pickle.load(handle)

def load_trial_stack(subject_idx):
    return np.load(f"filtered_stacks/filtered_stack_{subject_idx}.npy")

### TASK / NUll SPACE

def compute_subspaces(decoder):
    assert len(decoder.shape) == 2
    assert decoder.shape[0] < decoder.shape[1]
    _, _, Vt = np.linalg.svd(decoder, full_matrices=True, compute_uv=True)
    # the short side of the decoder, 2x64 in our task
    decoder_dim = decoder.shape[0]
    # task space and null space transposed
    return Vt.T[:,:decoder_dim].T, Vt.T[:,decoder_dim:].T

def mean_quadratic_form(C, subspace_basis):
    """
    used to find the mean variance in subspace dimensions
    for each row in x, compute x.T@A@x
    take the average over these quadratics

    subspace_basis : an orthonorm basis for subspace, vecs are in rows
    C : covariance or other matrix
    """
    # C is square, dimensions should align
    assert subspace_basis.shape[1] == C.shape[0]
    assert subspace_basis.shape[1] == C.shape[1]
    mean = 0
    dim_subspace = subspace_basis.shape[0]
    for u in subspace_basis:
        # convert to column vector
        u = u.reshape(-1, 1)
        # flatten the quadratic form into a number
        mean += (u.T @ C @ u).ravel()
    # flatten mean into a number
    return (mean / dim_subspace).ravel()


def subspace_projection(C, subspace):
    projection = np.empty(shape=(subspace.shape[0]))
    for i, dim in enumerate(subspace):
        projection[i] = dim.T @ C @ dim
    return projection


def mean_zero_cov(data):
    assert len(data.shape) == 2
    assert data.shape[1] == 64
    return (data.T @ data) / data.shape[0]


### MISC


def insert_into_1d(x, idx, val):
    out = np.empty(shape=x.shape[0] + 1)
    out[:idx] = x[:idx]
    out[idx] = val
    if idx != x.shape[0]:
        out[idx + 1 :] = x[idx:]
    return out


## NANS


def remove_nan_rows(x, return_idx=False):
    mask = ~np.isnan(x).any(axis=1)
    if return_idx:
        return x[mask, :], np.where(mask)[0]
    else:
        return x[mask, :]


def remove_nan_cols(x):
    mask = ~np.isnan(x).any(axis=0)
    return x[mask]


def count_nan(data):
    return np.count_nonzero(np.isnan(data))


def count_not_nan(data):
    return np.count_nonzero(~np.isnan(data))


## NATURAL MOVEMENT DATA


def get_movement_filenames(collection_name, subject_name, session_name):
    filenames = []
    with open(ROOT_METADATA_PATH / collection_name / "natural_movement.json") as fp:
        movements = json.load(fp)["movements"]

    for movement in movements:
        directory = (
            ROOT_RAWDATA_PATH
            / collection_name
            / subject_name
            / "natural_movement"
            / session_name
        )
        prefix = str(
            ROOT_RAWDATA_PATH
            / collection_name
            / subject_name
            / "natural_movement"
            / session_name
            / movement
        )
        for filename in directory.iterdir():
            if (
                str(filename).startswith(prefix)
                and str(filename).split(".")[-1] == "bin"
            ):
                filenames.append(filename)
    return filenames


def load_movement_emg(filename):
    return (
        np.fromfile(filename, dtype=np.int32).reshape(-1, 68).astype(np.float32)[:, :64]
    )


def find_nat_movement_active_indices(sig, std_multiple=1.0, min_indices=10):
    assert sig.shape[1] == 64
    sig_norms = np.linalg.norm(sig, axis=1)

    # find location of min trajectory norm (closest to zero)
    low_point = np.argmin(sig_norms)

    # stddev of the spatial norms
    sig_norm_std = np.std(sig_norms)

    # compute the threshold, mean of a short range around the low point
    mean_norm_threshold = np.mean(
        sig_norms[np.max([0, low_point - 5]) : low_point + 5], axis=0
    )

    # mask -- one std above the lowest norm point
    mask = sig_norms > mean_norm_threshold + sig_norm_std * std_multiple

    # return the indices
    if np.sum(mask) < min_indices:
        indices = np.arange(sig.shape[0])[-min_indices:]
    else:
        indices = np.arange(sig.shape[0])[mask]
    return indices, low_point, mean_norm_threshold


def load_movement_mean_stack(subject):
    """
        load all of a subject's movement data
        interleave the two sessions
    """
    movement_emg = np.empty(shape=(2, 14, 64))
    movement_emg[:] = np.nan

    for session_idx, session_name in enumerate(["session_0", "session_1"]):
        filenames = get_movement_filenames(
            "emg_olympics", subject.name, "natural_movement", session_name
        )
        for movement_idx, filename in enumerate(filenames):
            emg = load_movement_emg(filename)
            filtered = emg.filter_emg(emg, subject.variance)
            indices, low_point, mean_norm_threshold = find_nat_movement_active_indices(
                filtered
            )
            movement_emg[session_idx, movement_idx] = np.mean(filtered[indices] - filtered[low_point], axis=0)

    c = np.empty((28, movement_emg.shape[2]), dtype=movement_emg.dtype)
    c[0::2, :] = movement_emg[0]
    c[1::2, :] = movement_emg[1]

    return c


### CALIBRATION

def get_calibration_emg_filenames(collection_name, subject_name, session_name):
    directory = (
        ROOT_RAWDATA_PATH
        / collection_name
        / subject_name
        / "calibration_bars"
        / session_name
    )
    filenames = []
    for filename in directory.iterdir():
        if ("_emg_" in str(filename) and not "csv" in str(filename)):
            filenames.append(filename)
    filenames.sort(key=lambda x: int(x.name.split("/")[-1].split("_")[0]))
    return filenames


def get_calibration_bar_filenames(collection_name, subject_name, session_name):
    directory = (
        ROOT_RAWDATA_PATH
        / collection_name
        / subject_name
        / "calibration_bars"
        / session_name
    )
    filenames = []
    for filename in directory.iterdir():
        if ("_bars_" in str(filename) and not "csv" in str(filename)):
            filenames.append(filename)
    filenames.sort(key=lambda x: int(x.name.split("/")[-1].split("_")[0]))
    return filenames

def load_calibration_emg(filename):
    return (
        np.fromfile(filename, dtype=np.int32).reshape(-1, 68)[:,:64]
    )

def load_calibration_bar(filename):
    return (
        np.fromfile(filename, dtype=np.float32).reshape(-1, 64)
    )


### OLD STUFF


# def log(x, a, b):
#     return b * np.log(x) + a


# def calculate_hit_percentage(num_hits):
#     num_targets = 12
#     return 100 * num_hits / num_targets


# def get_outcomes(experiment, subject):
#     session_path_list = files.get_session_path_list(experiment, subject)
#     num_sessions = len(session_path_list)
#     hits = []
#     misses = []
#     noholds = []
#     reach_times = []
#     for behavior_path in session_path_list:
#         outcome_path = [x for x in behavior_path.iterdir() if "result" in x.name][0]
#         behavior = np.genfromtxt(
#             str(outcome_path), delimiter=",", skip_header=1, dtype=None, encoding=None
#         )
#         outcomes = [x[0] for x in behavior]
#         for x in behavior:
#             if x[0] == "Hit":
#                 reach_times.append(x[2])
#             elif x[0] == "Miss":
#                 reach_times.append(x[2])
#             else:
#                 reach_times.append(np.inf)
#         uniques, counts = np.unique(outcomes, return_counts=True)
#         for outcome, count in zip(uniques, counts):
#             if outcome == "Hit":
#                 hits.append(count)
#             elif outcome == "Miss":
#                 misses.append(count)
#             elif outcome == "No Hold":
#                 noholds.append(count)
#             else:
#                 raise ValueError("Unforeseen outcome in behavior: ", outcome)
#         if "Hit" not in outcomes:
#             hits.append(0)
#         if "Miss" not in outcomes:
#             misses.append(0)
#         if "No Hold" not in outcomes:
#             noholds.append(0)
#     return hits, misses, noholds, num_sessions, reach_times


# def plot_control_preview(data, decoder, ax, label=""):
#     ax.plot(np.dot(decoder[-1:],data.T)[0],np.dot(decoder[-2:-1],data.T)[0],label=label)
#     ax.plot(np.dot(decoder[-1:],data.T)[0].mean(),np.dot(decoder[-2:-1],data.T)[0].mean(),"o",label=label+"mean",zorder=10)

# def plot_dynamics_preview(data, dynamics, decoder, label=""):
#     fig, ax = plt.subplots(1,1)
#     states = []
#     state = np.zeros(shape=(6,1))
#     for sample in data:
#         state = utils.advance_dynamics(dynamics,state,decoder,sample.reshape(-1,1))
#         states.append(state)
#     states = np.hstack(states)
#     ax.set_ylim([-2,2])
#     ax.set_xlim([-2,2])
#     plot_box(ax)
#     # plot_control_preview(offset_movement_data, decoder, ax)
#     ax.plot(states[0],states[1])
#     ax.plot(states[0].mean(),states[1].mean(),"ro")
#     ax.legend()
#     return states


# def get_task_paths(subject_folder):
#     task_paths = {}
#     for x in subject_folder.iterdir():
#         if x.name[0] != ".":
#             task_paths[x.name] = x
#     return task_paths

# def get_outcome_path(block_path):
#     return [x for x in block_path.iterdir() if "result" in x.name][0]

# # behavior space trajectories
# def load_behavior(path):
#     return np.genfromtxt(path, delimiter=',', skip_header=1, dtype=float, encoding=None)

# experiment > subject > task > session > trial

# we want to index the data in one place by:
# experiment -- emg_olympics or emg_repeats
# task -- natural_movement, calibration_bars, center_hold

# rawdata /
# center_hold (45 sessions) / subject
#     session_N /
#        12 trials per session -- one per target
#        one result csv file -- "index_behavior_timestamp.csv"
#        emg bin -- "index_emg_timestampt.bin"
#        emg filtered -- "index_emg_filtered_timestamp.bin"
#        behavior csv -- "session_result_timestamp.csv"

# metadata / experiment / subject /
#     decoder.bin
#     dynamics.bin
#     metadata.json
#     nmf_model.pkl
#     offsets.bin
#     variance.bin

# natural_movement (2 sessions)
#     14 movements
#     emg bin
#     csv for cue timing (timestamps)

# calibration_bars (2 sessions)
#     32 trials
#     bar (behavior) bin
#     emg bin
#     bar order csv (random)

#
# class Subject():
#     def __init__(self):
#         self.sessions = []


# class Trial():
#     def __init__(self):
#         self.target_coordinate = None
#         self.outcome = None
#         self.hold_time = None
#         self.reach_time = None

#         self.idx = None
#         self.target_idx = None
#         self.session = None
#         self.behavior_path = None
#         self.emg_path = None

#     def parse_outcome(self, outcome):
#         self.target_coordinate = outcome["target"]
#         self.outcome = outcome["outcome"]
#         self.hold_time = outcome["hold_time"]
#         self.reach_time = outcome["reach_time"]

#     def parse_target(self, coord):
#         for idx, t in enumerate(self.targets):
#             if sum(abs(coord - t)) < 0.001:
#                 return idx

# class Session():
#     def __init__(self, path):
#         self.path = path
#         self.outcomes = self.get_outcomes()
#         self.trials = self.add_trials()
#         self.idx = int(path.name.split("_")[-1])
#         self.add_paths_to_trials()

#     def get_outcomes(self):
#         outcome_path = get_outcome_path(self.path)
#         # get something we can index
#         #  outcome, HT, RT, tX, tY
#         behavior = np.genfromtxt(str(outcome_path), delimiter=',', skip_header=1, dtype=None, encoding=None)
#         outcome_dict = {}
#         for i, x in enumerate(behavior):
#             outcome_dict[str(i)] = {}
#             outcome_dict[str(i)]["outcome"] = x[0]
#             outcome_dict[str(i)]["target"] = [x[-2],x[-1]]
#             outcome_dict[str(i)]["hold_time"] = x[1]
#             if x[0] == "Hit":
#                 outcome_dict[str(i)]["reach_time"] = x[2]
#             else:
#                 outcome_dict[str(i)]["reach_time"] = None
#         return outcome_dict

#     def add_trials(self):
#         trials = []
#         for _, outcome in self.outcomes.items(): # trial_path, trial_outcome in b.outcomes:
#             trial = Trial()
#             trial.parse_outcome(outcome)
#             trials.append(trial)
#         return trials

#     def add_paths_to_trials(self):
#         emg_paths = sorted([x for x in self.path.iterdir() if "emg" in x.name and "filtered" not in x.name and x.suffix == ".bin"], key=files.parse_filename_prefix)
#         filtered_paths = sorted([x for x in self.path.iterdir() if "emg" in x.name and "filtered" in x.name and x.suffix == ".bin"], key=files.parse_filename_prefix)
#         behavior_paths = sorted([x for x in self.path.iterdir() if "behavior" in x.name and x.suffix == ".csv"], key=files.parse_filename_prefix)
#         assert len(emg_paths) == len(self.trials), "mismatch between number of trials and number of paths"
#         assert len(filtered_paths) == len(self.trials), "mismatch between number of trials and number of paths"
#         assert len(behavior_paths) == len(self.trials), "mismatch between number of trials and number of paths"
#         for emg_path, filtered_path, behavior_path, trial in zip(emg_paths, filtered_paths, behavior_paths, self.trials):
#             trial.emg_path = emg_path
#             trial.filtered_path = filtered_path
#             trial.behavior_path = behavior_path
