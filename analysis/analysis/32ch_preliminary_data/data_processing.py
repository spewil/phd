import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("TkAgg")
import pickle
import numpy as np
import pandas as pd
import scipy
import collections.abc
from pathlib import Path
from utils import utils, files, analysis
from sklearn.decomposition import PCA
from sklearn.decomposition import NMF
from sklearn.decomposition import FastICA

# for each session
#   for each block
#     for each trial

# questions:
# - are finger movements low dimensional?
#       - run PCA on all, compare
# - are the low dimensional features reliable over days?
#       - visually inspect
#       - measure of similarity between features
# -
"""

I need to be able to use the same task mappings across days in order to track learning over days.
This data should tell me if the features of the movements are stable across days. If the features
are stable, then I can use those same features across days to build mappings for cross-session learning.

"""

base_folder = Path("/Users/spencerw/data/32_channel_andy_dec_2020/fingers")
fingers = [
    "index_flex", "middle_flex", "ring_flex", "pinky_flex", "index_ext",
    "middle_ext", "ring_ext", "pinky_ext"
]
flex = " flexion"
ext = " extension"
finger_labels = [
    "index" + flex, "middle" + flex, "ring" + flex, "pinky" + flex,
    "index" + ext, "ring" + ext, "middle" + ext, "pinky" + ext
]


def save_dict(data, filestem, format="pickle"):
    if format == "json":
        json.dump(data, open(filestem + ".json", 'w'))
    elif format == "pickle":
        with open(filestem + '.pkl', 'wb') as f:
            pickle.dump(data, f)  #, pickle.HIGHEST_PROTOCOL)


def load_dict(filestem, format="pickle"):
    if format == "json":
        data = json.load(open(filestem + ".json"))
    elif format == "pickle":
        with open(filestem + ".pkl", 'rb') as f:
            return pickle.load(f)


def parse_timestamp(path):
    return int(path.stem.partition("T")[-1].replace("_", ""))


def build_finger_movement_path_dictionary(folder_path):
    session_paths = files.list_folders(folder_path)
    # sort by date
    session_paths.sort(key=lambda x: x.name[0])
    block_paths = ["1", "2", "3"]
    trial_paths_by_finger = {}
    for finger in fingers:
        trial_paths_by_finger[finger] = []
    # print(f"sessions: {len(session_paths)}")
    # print(f"sessions per session: {len(session_paths)}")
    for session in session_paths:
        for block in block_paths:
            trial_paths = files.list_files(session / block, ext=".bin")
            trial_paths.sort(key=parse_timestamp)
            # each trial is 8 finger movements: four flexion and four extension
            for i, finger in enumerate(fingers):
                trial_paths_by_finger[finger].append(trial_paths[i])
    return trial_paths_by_finger


def build_finger_movement_trajectory_dictionary(path_dict, preprocess=True):
    finger_trajectories = {}
    for finger in fingers:
        trajectories = []
        for path in path_dict[finger]:
            d = files.load_from_bin_file(path)
            if preprocess:
                pp = analysis.preprocess_emg(d)
                trajectories.append(pp)
            else:
                trajectories.append(d)
        finger_trajectories[finger] = np.array(trajectories)
    return finger_trajectories


def compute_NMF_components(array, n_comps=1):
    """
        gives weights and components
        input must be samples x channels
        X = WH 
        W is fit_transform --> component weights for each sample, 
        H are components_
    """
    assert array.shape[0] > array.shape[1]
    nmf = NMF(n_components=n_comps)
    nmf.fit(array)
    return nmf.components_


def build_finger_movement_NMF_dictionary(trajectory_dict):
    finger_components = {}
    for finger in fingers:
        components = []
        for trajectory in trajectory_dict[finger]:
            components.append(compute_NMF_components(trajectory.T))
        finger_components[finger] = np.array(components)
    return finger_components


def compute_top_PCA_component(array, pca=None):
    if pca is None:
        pca = PCA()
    pca.fit(array)
    return pca.components_[0, :]


def build_PCA_feature_dict(trajectory_dict):
    finger_components = {}
    pca = PCA()
    for finger in fingers:
        components = []
        for trajectory in trajectory_dict[finger]:
            components.append(compute_top_PCA_component(trajectory.T, pca))
        finger_components[finger] = np.array(components)
    return finger_components


def compute_PCA_variance(array, pca=None):
    if pca is None:
        pca = PCA()
    pca.fit(array)
    return pca.explained_variance_ratio_


def build_PCA_variance_dict(trajectory_dict):
    PCA_variance_dict = {}
    pca = PCA()
    for finger in fingers:
        PCA_variance_dict[finger] = []
        for t in trajectory_dict[finger]:
            PCA_variance_dict[finger].append(compute_PCA_variance(t.T,
                                                                  pca=pca))
        PCA_variance_dict[finger] = np.array(PCA_variance_dict[finger])
    return PCA_variance_dict


def distance_matrix(X, metric="cosine"):
    # X is observations x dimensions
    return scipy.spatial.distance.squareform(
        scipy.spatial.distance.pdist(X, metric))


def parse_data_filepath(path, year=2020):
    """
        file name convention changes between block 1 and blocks 2 and 3
    """
    if "behavior" in path.name:
        return None, None, "behavior"
    direction_str = "_direction_"
    trial_str = "_trial_"
    year_str = str(year) + "-"
    direction_idx = path.name.find(direction_str)
    trial_idx = path.name.find(trial_str)
    if trial_idx == -1:
        raise ValueError(f"Parse failed, no trial string in {path.name}")
    if direction_idx == -1:
        raise ValueError(f"Parse failed, no direction string in {path.name}")
    target_direction = int(path.name[direction_idx +
                                     len(direction_str):trial_idx])
    if path.suffix == ".bin":
        filetype = "emg"
        year_idx = path.name.find(year_str)
        if path.name[year_idx - 1] == "_":
            year_idx -= 2
        if year_idx == -1:
            raise ValueError(f"Parse failed, no year string in {path.name}")
        trial_number = int(path.name[trial_idx + len(trial_str):year_idx])
    elif path.suffix == ".csv":
        filetype = "task"
        if path.stem[-1] == "_":
            trial_number = int(path.stem[trial_idx + len(trial_str):-2])
        else:
            trial_number = int(path.stem[trial_idx + len(trial_str):])
    return trial_number, target_direction, filetype


def update(d, u):
    """
    Update existing dictionary d with new dict with parallel structure
    https://stackoverflow.com/questions/3232943/update-value-of-a-nested-dictionary-of-varying-depth
    """
    for k, v in u.items():
        if isinstance(v, collections.abc.Mapping):
            d[k] = update(d.get(k, {}), v)
        else:
            d[k] = v
    return d


def build_center_hold_dict():
    center_hold_data_path = Path(
        "/Users/spencerw/data/32_channel_andy_dec_2020/center_hold")
    center_hold_dict = {}
    for block in blocks:
        block_int = int(block)
        for path in files.list_files((center_hold_data_path / str(block))):
            trial, direction, filetype = parse_data_filepath(path)
            if filetype == "behavior":
                dict_update = {
                    block_int: {
                        "behavior": {
                            "path": path,
                            "data": pd.read_csv(path)
                        }
                    }
                }
            elif filetype == "task":
                dict_update = {
                    block_int: {
                        "trials": {
                            trial: {
                                "task": {
                                    "path": path,
                                    # columns aren't labeled correctly
                                    # skip first row and label manually
                                    "data": pd.read_csv(path, skiprows=1)
                                },
                                "direction": direction
                            }
                        }
                    }
                }
            elif filetype == "emg":
                dict_update = {
                    block_int: {
                        "trials": {
                            trial: {
                                "emg": {
                                    "path": path,
                                    "data": files.load_from_bin_file(path)
                                },
                            }
                        }
                    }
                }
            else:
                raise (ValueError(f"Filetype {filetype} not valid."))
            center_hold_dict = update(center_hold_dict, dict_update)
    return center_hold_dict


def build_task_PCA_variance_dict():
    center_hold_dict = load_dict("center_hold_12_9")
    pca = PCA()
    center_hold_PCA_variance_dict = {}
    for block in blocks:
        center_hold_PCA_variance_dict[block] = {}
        for trial_no, trial_dict in sorted(
                center_hold_dict[block]["trials"].items()):
            emg_array = trial_dict["emg"]["data"][:32]
            preprocessed_emg = analysis.preprocess_emg(emg_array)
            pca.fit(preprocessed_emg)
            center_hold_PCA_variance_dict[block][
                trial_no] = pca.explained_variance_ratio_
    return center_hold_PCA_variance_dict


def build_concat_task_PCA_variance_dict():
    center_hold_dict = load_dict("center_hold_12_9")
    pca = PCA()
    center_hold_concat_PCA_variance_dict = {}
    for block in blocks:
        emg_list = []
        for trial_no, trial_dict in sorted(
                center_hold_dict[block]["trials"].items()):
            emg_array = trial_dict["emg"]["data"][:32]
            emg_list.append(emg_array)
        emg_concat = np.hstack(emg_list)
        print(emg_concat.shape)
        preprocessed_emg = analysis.preprocess_emg(emg_concat)
        pca.fit(preprocessed_emg)
        center_hold_concat_PCA_variance_dict[
            block] = pca.explained_variance_ratio_
    return center_hold_concat_PCA_variance_dict


blocks = [1, 2, 3]
if __name__ == "__main__":
    ### Build raw data trials by finger in chronological order
    trial_paths_by_finger = build_finger_movement_path_dictionary(base_folder)
    raw_data_dict = build_finger_movement_trajectory_dictionary(
        trial_paths_by_finger, preprocess=False)
    save_dict(raw_data_dict, "finger_data")

    ### preprocess raw data
    trajectory_dict = build_finger_movement_trajectory_dictionary(
        trial_paths_by_finger)
    save_dict(trajectory_dict, "finger_trajectories")

    ### compute features of preprocessed trajectories
    PCA_feature_dict = build_PCA_feature_dict(trajectory_dict)
    save_dict(PCA_feature_dict, "finger_PCA_features")
    PCA_variance_dict = build_PCA_variance_dict(trajectory_dict)
    save_dict(PCA_variance_dict, "finger_PCA_variances")

    ### center hold data

    center_hold_data = build_center_hold_dict()
    save_dict(center_hold_data, "center_hold_12_9")

    task_PCA_variance_dict = build_task_PCA_variance_dict()
    save_dict(task_PCA_variance_dict, "task_PCA_variance")
    task_concat_PCA_variance_dict = build_concat_task_PCA_variance_dict()
    save_dict(task_concat_PCA_variance_dict, "task_concat_PCA_variance")