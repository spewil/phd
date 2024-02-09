import boto3
import numpy as np
from io import StringIO
from pathlib import Path
import json
import sys

### S3

s3_resource = boto3.resource("s3")
s3 = boto3.client("s3")
bucket_name = "motorlearning"
bucket = s3_resource.Bucket(name=bucket_name)

if sys.platform == "linux":
    ROOT_RAWDATA_PATH = Path("/home/spencer/motor-control/data/rawdata/")
    ROOT_METADATA_PATH = Path("/home/spencer/motor-control/data/metadata/")  
else:   
    ROOT_RAWDATA_PATH = Path("/Users/spencer/motor-control/data/rawdata/")
    ROOT_METADATA_PATH = Path("/Users/spencer/motor-control/data/metadata/")

def get_decoder(subject):
    return subject.decoder[-2:,:]

def get_subject_names(collection_name):
    # get all subject names in an experiment
    decoder_object_name = f"metadata/{collection_name}"
    metadata_objects: dict = s3.list_objects(
        Bucket=bucket_name, Prefix=decoder_object_name
    )
    names = []
    for obj in metadata_objects["Contents"]:
        split_obj = obj["Key"].split("/")
        if len(split_obj) > 3:
            possible_name = split_obj[2]
            if possible_name in names or possible_name in ["peter"]:
                continue
            else:
                names.append(possible_name)
    return names


def list_objects(prefix):
    try:
        l = [
            o["Key"]
            for o in s3.list_objects(Bucket="motorlearning", Prefix=prefix)["Contents"]
        ]
        l.sort()
        return l
    except:
        print(f"Unable to find object with prefix {prefix}.")


def get_objects(key):
    try:
        blob = s3.get_object(Bucket="motorlearning", Key=key)["Body"].read()
    except:
        print(f"Unable to find object with key {key}.")


### TARGETS


def generate_target_angles():
    return (np.linspace(0, 2 * np.pi, 13))[:-1]


def compute_theta(vec):
    vec = np.array(vec)
    if vec.shape[0] != 2:
        raise ValueError(f"array has incorrect shape, {vec.shape}")
    angle = np.arctan2(vec[1], vec[0])
    if vec[1] < 0:
        angle += 2 * np.pi
    return angle


def compute_target_vec_from_number(target_number):
    # targets numbered 1..12
    assert target_number > 0 and target_number < 13
    angles = generate_target_angles()
    return np.round(
        np.array(
            [np.cos(angles[target_number - 1]), np.sin(angles[target_number - 1])]
        ),
        2,
    )


def compute_target_number_from_vec(vec):
    angles = generate_target_angles()
    theta = compute_theta(vec)
    return np.abs(angles - theta).argmin() + 1


### COLLECTION


class Collection:
    # TODO
    # - get metadata here for the collection as well (ITI, etc. ) + metadata/collection/.JSONs
    # - do the subjects listed in metadata/collection/subjects match the rawdata?

    def __init__(self, collection_name) -> None:
        self.name = collection_name
        self.metadata = self.get_metadata()
        self.get_subject_names()  # subject_name : session_dict
        self.get_subjects()

    def get_metadata(self):
        collection_metadata_path = ROOT_METADATA_PATH / self.name / "metadata.json"
        with open(collection_metadata_path) as f:
            return json.load(f)

    def get_subject_names(self, local=True):
        if local:
            self.subject_names = [
                p.stem
                for p in (ROOT_RAWDATA_PATH / self.name).iterdir()
                if not "DS_Store" in p.name
            ]
        else:
            object_prefix = f"rawdata/{self.name}/"
            try:
                paths = s3.list_objects_v2(
                    Bucket="motorlearning", Prefix=object_prefix, Delimiter="/"
                )
                self.subject_names = [
                    p.get("Prefix").split("/")[-2] for p in paths.get("CommonPrefixes")
                ]
            except:
                raise ValueError(f"Unable to find object with prefix {object_prefix}")
        self.subject_names.sort()

    def get_subjects(self):
        self.subjects = {}
        for subject_name in self.subject_names:
            self.subjects.update({subject_name: Subject(self.name, subject_name)})

    def alphabetically_sorted_subjects(self):
        return sorted(list(self.subjects.values()), key=lambda s: s.name)


class Subject:
    def __init__(self, collection_name, subject_name) -> None:
        self.collection_name = collection_name
        self.name = subject_name
        self.decoder = self.get_decoder()  # /metadata/collection/subject/decoder.bin
        self.variance = self.get_variance()  # /metadata/collection/subject/variance.bin
        self.offsets = self.get_offsets()  # /metadata/collection/subject/offsets.bin
        self.dynamics = self.get_dynamics()  # /metadata/collection/subject/dynamics.bin
        self.nmf_components = (
            self.get_nmf_components()
        )  # /metadata/collection/subject/metadata.json
        self.task_subspace, self.null_subspace = self.compute_subspaces()
        self.get_task_names()
        self.get_tasks()

    def compute_subspaces(self):
        # https://math.stackexchange.com/questions/1771013/how-is-the-null-space-related-to-singular-value-decomposition?rq=1
        # the first two eigenvectors are the subspace spanning Col(D), the rest are Null(D)
        assert len(self.decoder.shape) == 2
        assert self.decoder.shape[0] < self.decoder.shape[1]
        # make sure to truncate the full decoder
        _, _, Vt = np.linalg.svd(
            self.decoder[-2:, :], full_matrices=True, compute_uv=True
        )
        # the short side of the decoder, 2x64 in our task
        decoder_dim = 2
        # task space and null space transposed
        return Vt.T[:, :decoder_dim].T, Vt.T[:, decoder_dim:].T

    def get_task_names(self, local=True):
        if local:
            self.task_names = [
                p.stem
                for p in (
                    ROOT_RAWDATA_PATH / self.collection_name / self.name
                ).iterdir()
                if not "DS_Store" in p.name
            ]
        else:
            object_prefix = f"rawdata/{self.collection_name}/{self.name}/"
            try:
                paths = s3.list_objects_v2(
                    Bucket="motorlearning", Prefix=object_prefix, Delimiter="/"
                )
                self.task_names = [
                    p.get("Prefix").split("/")[-2] for p in paths.get("CommonPrefixes")
                ]
            except:
                raise ValueError(f"Unable to find object with prefix {object_prefix}")

    def get_tasks(self):
        self.tasks = {}
        for task_name in self.task_names:
            if task_name == "center_hold":
                self.tasks[task_name] = Task(self.collection_name, self.name, task_name)

    def get_decoder(self, local=True):
        # load subject's decoder and store in memory as numpy array
        # decoders are 6x64 dimensional
        # decoder_object_name = f"metadata/{self.collection_name}/{self.subject_name}/decoder.bin"
        # decoder_object = s3.get_object(Bucket='motorlearning', Key=decoder_object_name)
        # binblob = decoder_object["Body"].read()
        # self.decoder = np.frombuffer(binblob, dtype='<f4').reshape(-1,64)
        if local:
            decoder_path = (
                ROOT_METADATA_PATH / self.collection_name / self.name / "decoder.bin"
            )
            return np.fromfile(decoder_path, dtype="<f4").reshape(-1, 64)
        else:
            return None

    def get_variance(self):
        # load subject's recorded variance file and store in memory as numpy array
        variance_path = (
            ROOT_METADATA_PATH / self.collection_name / self.name / "variance.bin"
        )
        return np.fromfile(variance_path, dtype="<f4").reshape(-1, 64)

    def get_offsets(self):
        # load subject's recorded variance file and store in memory as numpy array
        offsets_path = (
            ROOT_METADATA_PATH / self.collection_name / self.name / "offsets.bin"
        )
        return np.fromfile(offsets_path, dtype="<f4").reshape(-1, 64)

    def get_dynamics(self):
        dynamics_path = (
            ROOT_METADATA_PATH / self.collection_name / self.name / "dynamics.bin"
        )
        return np.fromfile(dynamics_path, dtype="<f4").reshape(-1, 6)

    def get_nmf_components(self):
        subject_metadata_path = (
            ROOT_METADATA_PATH / self.collection_name / self.name / "metadata.json"
        )
        with open(subject_metadata_path) as f:
            metadata = json.load(f)
        return metadata["components"]


class Task:
    def __init__(self, collection_name, subject_name, task_name) -> None:
        self.collection_name = collection_name
        self.subject_name = subject_name
        self.name = task_name
        self.get_session_names()
        self.get_sessions()

    def get_session_names(self, local=True):
        if local:
            self.session_names = [
                p.stem
                for p in (
                    ROOT_RAWDATA_PATH
                    / self.collection_name
                    / self.subject_name
                    / self.name
                ).iterdir()
                if not "DS_Store" in p.name
            ]
        else:
            object_prefix = (
                f"rawdata/{self.collection_name}/{self.subject_name}/{self.name}/"
            )
            try:
                paths = s3.list_objects_v2(
                    Bucket="motorlearning", Prefix=object_prefix, Delimiter="/"
                )
                self.session_names = [
                    p.get("Prefix").split("/")[-2] for p in paths.get("CommonPrefixes")
                ]
            except:
                raise ValueError(f"Unable to find object with prefix {object_prefix}")

    def get_sessions(self):
        self.sessions = {}
        for session_name in self.session_names:
            session_number = int(session_name.split("_")[-1])
            # exceptions for the center hold dataset
            if self.name == "center_hold":
                if self.subject_name == "svenja":
                    # svenja's session numbering is +1 (1,2,3 .. 45) so grab all of these
                    self.sessions[session_name] = Session(
                        self.collection_name,
                        self.subject_name,
                        self.name,
                        f"session_{session_number}",
                    )
                # only for sessions below 45
                if session_number <= 44:
                    # hyewon's first session was ended early, so we skip it
                    # andrei's session_11 is empty, so we skip it by going one higher than 11
                    if self.subject_name == "hyewon" or (
                        self.subject_name == "andrei" and session_number >= 11
                    ):
                        self.sessions[session_name] = Session(
                            self.collection_name,
                            self.subject_name,
                            self.name,
                            f"session_{session_number+1}",
                        )
                    else:
                        self.sessions[session_name] = Session(
                            self.collection_name,
                            self.subject_name,
                            self.name,
                            f"session_{session_number}",
                        )

    def sorted_sessions(self):
        return sorted(list(self.sessions.values()), key=lambda s: s.number)


class Session:
    def __init__(self, collection_name, subject_name, task_name, session_name) -> None:
        self.collection_name = collection_name
        self.subject_name = subject_name
        self.task_name = task_name
        self.name = session_name
        self.number = int(session_name.split("_")[-1])
        self.outcome_counts = {}
        self.trial_names = []
        self.trials = {}  # named with ordinals trial_0, trial_1, ...
        self.get_outcome_array()
        self.parse_outcomes_into_trials()

    def get_outcome_array(self, local=True):
        """
        get the behavior file for the session
        use this to generate trial names
        if the outcome is No Hold the trial number will be the same
        record the nominal trial number and the recorded trial number
        """
        try:
            self.outcome_array.shape
        except AttributeError:
            self.outcome_array = np.ndarray([])
        # if data is there, return
        else:
            return

        if local:
            directory = (
                ROOT_RAWDATA_PATH
                / self.collection_name
                / self.subject_name
                / self.task_name
                / self.name
            )
            prefix = f"{ROOT_RAWDATA_PATH / self.collection_name / self.subject_name / self.task_name / self.name}/session_result"
            try:
                outcome_path = [
                    f for f in directory.iterdir() if str(f).startswith(prefix)
                ][0]
            except IndexError:
                raise ValueError(f"No file found with prefix {prefix}")
            self.outcome_array = np.genfromtxt(
                str(outcome_path),
                delimiter=",",
                skip_header=1,
                dtype=None,
                encoding=None,
            )
        # pull session behavior data from s3
        else:
            object_prefix = f"rawdata/{self.collection_name}/{self.subject_name}/{self.task_name}/{self.name}/session_result_"
            try:
                object_key = s3.list_objects(
                    Bucket="motorlearning", Prefix=object_prefix
                )["Contents"][0]["Key"]
            except:
                print(
                    f"Unable to find object with name {self.subject_name} and prefix {object_prefix}."
                )
                return None
            try:
                blob = s3.get_object(Bucket="motorlearning", Key=object_key)[
                    "Body"
                ].read()
            except:
                print(f"Unable to find object with key {object_key}.")
                return None
            self.outcome_array = np.genfromtxt(
                StringIO(blob.decode("utf-8")),
                delimiter=",",
                skip_header=1,
                dtype=None,
                encoding=None,
            )
            if self.outcome_array.size == 0:
                print(f"the file with key {object_key} is empty!")

    def parse_outcomes_into_trials(self):
        for trial_idx, line in enumerate(self.outcome_array):
            trial_name = f"trial_{str(trial_idx)}"
            self.trial_names.append(trial_name)
            trial = Trial(
                self.collection_name,
                self.subject_name,
                self.task_name,
                self.name,
                trial_name,
            )
            trial.set_number(trial_idx)
            trial.set_outcome(line[0])
            trial.set_target([line[-2], line[-1]])
            # the "no hold number" is the number within the set of files with the same recorded number prefix
            # i.e. there may be more than one file with the prefix "10_behavior" due to a no hold
            # first trial sync up the numbers
            if trial_idx == 0:
                target_coords = [0, 0]
                recorded_number = 0
                no_hold_block_number = 0
            # after first trial, if target has changed
            elif trial.target_coords != target_coords:
                # increment "real" counter
                recorded_number += 1
                # reset no hold counter
                no_hold_block_number = 0
            else:
                # if we're still in the no hold block, increment
                no_hold_block_number += 1
            trial.set_recorded_number(recorded_number)
            trial.set_no_hold_number(no_hold_block_number)
            # keep target coords up to date
            target_coords = trial.target_coords
            target_coords = [line[-2], line[-1]]
            trial.set_hold_time(line[1])
            if trial.outcome == "Hit":
                trial.set_reach_time(line[2])
            else:
                trial.set_reach_time(None)
            if trial.outcome != "No Hold":
                (
                    trial.active_indices,
                    trial.low_point,
                    _,
                ) = trial.find_active_indices()
            self.trials.update({trial_name: trial})

        # count unique outcomes
        outcomes = [line[0] for line in self.outcome_array]
        uniques, counts = np.unique(outcomes, return_counts=True)
        for outcome, count in zip(uniques, counts):
            if outcome == "Hit":
                self.outcome_counts["hits"] = count
            elif outcome == "Miss":
                self.outcome_counts["misses"] = count
            elif outcome == "No Hold":
                self.outcome_counts["noholds"] = count
            else:
                raise ValueError("Unforeseen outcome in behavior: ", outcome)
        # if outcome didn't happen, put a 0
        if "Hit" not in outcomes:
            self.outcome_counts["hits"] = 0
        if "Miss" not in outcomes:
            self.outcome_counts["misses"] = 0
        if "No Hold" not in outcomes:
            self.outcome_counts["noholds"] = 0

    def sorted_trials(self):
        return sorted(list(self.trials.values()), key=lambda t: t.number)


class Trial:
    def __init__(
        self, collection_name, subject_name, task_name, session_name, trial_name
    ) -> None:
        self.collection_name = collection_name
        self.subject_name = subject_name
        self.task_name = task_name
        self.session_name = session_name
        self.name = trial_name  # trial_0: str
        self.number = None  # 0: int
        self.recorded_number = None  # 0: int
        self.outcome = None  # "No Hold"
        self.trajectory_filename = None  # XXXX.bin
        self.trajectory = None  # ndarray
        self.filtered_emg_filename = None  # XXXX.bin
        self.filtered_emg = None  # ndarray
        self.raw_emg_filename = None  # XXXX.bin
        self.raw_emg = None  # ndarray
        self.active_indices = None
        self.low_point = None

    def find_active_indices(self, std_multiple=1.0, min_indices=10):
        assert self.outcome != "No Hold"
        # get trial signals
        hold_steps = int(200 * self.hold_time)
        traj = self.get_trajectory()[:, -2:].copy()
        sig = self.get_filtered_emg().copy()
        # adjust lengths to match
        min_length = np.min([traj.shape[0], sig.shape[0]])
        traj = traj[:min_length, :]
        sig = sig[:min_length, :]
        # get rid of channel 56, it's garbage
        sig[:, 56] = 0
        # find location of min trajectory norm (closest to zero)
        # only from the hold step period
        low_point = np.argmin(np.linalg.norm(traj[:hold_steps, :], axis=1))
        # find signal norm value at this point
        sig_norms = np.linalg.norm(sig, axis=1)
        sig_norm_std = np.std(sig_norms)
        # compute the threshold, mean of a short range
        mean_norm_threshold = np.mean(
            sig_norms[np.max([0, low_point - 5]) : low_point + 5], axis=0
        )
        # mask -- one std above the lowest norm point
        mask = sig_norms > mean_norm_threshold + sig_norm_std * std_multiple
        # ignore the hold period
        mask[:hold_steps] = False
        # return the indices
        min_num_indices = min_indices
        if np.sum(mask) < min_num_indices:
            indices = np.arange(sig.shape[0])[-min_num_indices:]
        else:
            indices = np.arange(sig.shape[0])[mask]
        return indices, low_point, mean_norm_threshold

    def set_outcome(self, outcome):
        self.outcome = outcome

    def set_target(self, target_coords):
        self.target_coords = target_coords
        self.target_number = compute_target_number_from_vec(self.target_coords)
        self.target_theta = compute_theta(self.target_coords)

    def set_hold_time(self, hold_time):
        self.hold_time = hold_time

    def set_reach_time(self, reach_time):
        self.reach_time = reach_time

    def set_number(self, number):
        self.number = number

    def set_recorded_number(self, recorded_number):
        self.recorded_number = recorded_number

    def set_no_hold_number(self, no_hold_number):
        self.no_hold_number = no_hold_number

    # # # #

    def get_trajectory_filename(self):
        if self.trajectory_filename is None:
            self.set_trajectory_filename()
        return self.trajectory_filename

    def set_trajectory_filename(self, local=True):
        if local:
            directory = (
                ROOT_RAWDATA_PATH
                / self.collection_name
                / self.subject_name
                / self.task_name
                / self.session_name
            )
            prefix = f"{ROOT_RAWDATA_PATH / self.collection_name / self.subject_name / self.task_name / self.session_name / str(self.recorded_number)}_behavior_"
            filename_list = [
                f for f in directory.iterdir() if str(f).startswith(prefix)
            ]
            filename_list.sort()
        else:
            object_prefix = f"rawdata/{self.collection_name}/{self.subject_name}/{self.task_name}/{self.session_name}/{self.recorded_number}_behavior_"
            filename_list = list_objects(prefix=object_prefix)
            # index by the number of the no hold block (almost always 0)
        self.trajectory_filename = filename_list[self.no_hold_number]

    def get_trajectory(self):
        if self.trajectory_filename is None:
            self.set_trajectory_filename()
        if self.trajectory is None:
            self.set_trajectory()
        return self.trajectory

    def set_trajectory(self, local=True):
        # get task space trajectory for a given experiment, subject, task, session, trial
        # time [sec], x, y [screen coords]
        if local:
            self.trajectory = np.genfromtxt(
                self.trajectory_filename,
                delimiter=",",
                skip_header=1,
                dtype=float,
                usecols=(1, 2, 3),
                encoding=None,
            )
        else:
            try:
                blob = s3.get_object(
                    Bucket="motorlearning", Key=self.trajectory_filename
                )["Body"].read()
            except:
                raise ValueError(
                    f"Unable to find object with prefix {self.trajectory_filename}"
                )
            self.trajectory = np.genfromtxt(
                StringIO(blob.decode("utf-8")),
                delimiter=",",
                skip_header=1,
                dtype=float,
                usecols=(1, 2, 3),
                encoding=None,
            )
        self.trajectory = self.trajectory[:, -2:]

    def get_filtered_emg_filename(self):
        if self.filtered_emg_filename is None:
            self.set_filtered_emg_filename()
        return self.filtered_emg_filename

    def set_filtered_emg_filename(self, local=True):
        # looks like: 11_emg_filtered_2021-09-16T18_10_31.bin
        if local:
            directory = (
                ROOT_RAWDATA_PATH
                / self.collection_name
                / self.subject_name
                / self.task_name
                / self.session_name
            )
            prefix = f"{ROOT_RAWDATA_PATH / self.collection_name / self.subject_name / self.task_name / self.session_name / str(self.recorded_number)}_emg_filtered_"
            filename_list = [
                f for f in directory.iterdir() if str(f).startswith(prefix)
            ]
            filename_list.sort()
        else:
            raise NotImplementedError("s3 access isn't implemented")
        self.filtered_emg_filename = filename_list[self.no_hold_number]

    def get_filtered_emg(self):
        if self.filtered_emg_filename is None:
            self.set_filtered_emg_filename()
        if self.filtered_emg is None:
            self.set_filtered_emg()
        return self.filtered_emg

    def set_filtered_emg(self, local=True):
        """
        load subject's filtered EMG
        from a particular collection, experiment, trial
        and store in memory as numpy array
        data is num_samples X 64 dimensional
        """
        if local:
            self.filtered_emg = np.fromfile(
                self.filtered_emg_filename, dtype=np.float32
            ).reshape(-1, 64)
        else:
            emg_object_name = f"rawdata/{self.collection_name}/{self.subject_name}/{self.task_name}/session_{self.session_name}/{self.name}_emg_filtered"
            matching_emg_objects = s3.list_objects(
                Bucket="motorlearning", Prefix=emg_object_name
            )
            if len(matching_emg_objects["Contents"]) > 1:
                raise ValueError(
                    f"More than one object found with prefix {emg_object_name}"
                )
            emg_object_name = matching_emg_objects["Contents"][0]["Key"]
            emg_object = s3.get_object(Bucket="motorlearning", Key=emg_object_name)
            binblob = emg_object["Body"].read()
            return np.frombuffer(binblob, dtype="<f4").reshape(-1, 64)

    # # # #

    def get_raw_emg_filename(self):
        if self.raw_emg_filename is None:
            self.set_raw_emg_filename()
        return self.raw_emg_filename

    def set_raw_emg_filename(self, local=True):
        # looks like: 11_emg_2021-09-16T18_10_31.bin
        if local:
            directory = (
                ROOT_RAWDATA_PATH
                / self.collection_name
                / self.subject_name
                / self.task_name
                / self.session_name
            )
            prefix = f"{ROOT_RAWDATA_PATH / self.collection_name / self.subject_name / self.task_name / self.session_name / str(self.recorded_number)}_emg_2021"
            filename_list = [
                f for f in directory.iterdir() if str(f).startswith(prefix)
            ]
            filename_list.sort()
        else:
            raise NotImplementedError("s3 access isn't implemented")
        self.raw_emg_filename = filename_list[self.no_hold_number]

    def get_raw_emg(self):
        if self.raw_emg_filename is None:
            self.set_raw_emg_filename()
        if self.raw_emg is None:
            self.set_raw_emg()
        return self.raw_emg

    def set_raw_emg(self, local=True):
        """
        load subject's raw (unfiltered) EMG
        from a particular collection, experiment, trial
        and store in memory as numpy array
        data is num_samples X 68 dimensional
        last four dimensions are from recording device
        and include a counter channel to show dropped samples
        """
        if local:
            self.raw_emg = (
                np.fromfile(self.raw_emg_filename, dtype=np.int32)
                .reshape(-1, 68)
                .astype(np.float32)
            )

        else:
            emg_object_name = f"rawdata/{self.collection_name}/{self.subject_name}/{self.task_name}/session_{self.session_name}/{self.name}_emg_2021"
            matching_emg_objects = s3.list_objects(
                Bucket="motorlearning", Prefix=emg_object_name
            )
            if len(matching_emg_objects["Contents"]) > 1:
                raise ValueError(
                    f"More than one object found with prefix {emg_object_name}"
                )
            emg_object_name = matching_emg_objects["Contents"][0]["Key"]
            emg_object = s3.get_object(Bucket="motorlearning", Key=emg_object_name)
            binblob = emg_object["Body"].read()
            return np.frombuffer(binblob, dtype="<f4").reshape(-1, 68)
