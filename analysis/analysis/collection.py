import boto3
import numpy as np 
from io import StringIO 
from analysis import analysis

s3_resource = boto3.resource('s3')
s3 = boto3.client("s3")
bucket_name = "motorlearning"
bucket = s3_resource.Bucket(name=bucket_name)


def get_subject_names(collection_name):
    # get all subject names in an experiment
    decoder_object_name = f"metadata/{collection_name}"
    metadata_objects: dict = s3.list_objects(Bucket=bucket_name, Prefix=decoder_object_name)
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
        l = [o["Key"] for o in s3.list_objects(Bucket='motorlearning', Prefix=prefix)["Contents"]]
        l.sort()
        return l
    except:
        print(f"Unable to find object with prefix {prefix}.")

def get_objects(key):
    try:
        blob = s3.get_object(Bucket='motorlearning', Key=key)["Body"].read()
    except:
        print(f"Unable to find object with key {key}.")

class Collection():
    # TODO
    # - get metadata here for the collection as well (ITI, etc. ) + metadata/collection/.JSONs
    # - do the subjects listed in metadata/collection/subjects match the rawdata?

    def __init__(self, collection_name) -> None:
        self.name = collection_name
        self.get_subject_names() # subject_name : session_dict
        self.get_subjects()

    def get_subject_names(self):
        object_prefix = f"rawdata/{self.name}/"
        try:
            paths = s3.list_objects_v2(Bucket='motorlearning', Prefix=object_prefix, Delimiter="/")
            self.subject_names = [p.get("Prefix").split("/")[-2] for p in paths.get("CommonPrefixes")]
        except:
            raise ValueError(f"Unable to find object with prefix {object_prefix}")
        self.subject_names.sort()
        self.subjects = {}
        for subject_name in self.subject_names:
            self.subjects[subject_name] = None

    def get_subjects(self):
        for subject_name in self.subject_names:
            self.subjects.update({subject_name: Subject(self.name, subject_name)})

    def alphabetically_sorted_subjects(self):
        return sorted(list(self.subjects.values()), key= lambda s: s.name)


class Subject():
    def __init__(self, collection_name, subject_name) -> None:
        self.collection_name = collection_name
        self.name = subject_name 
        self.get_decoder() # /metadata/collection/subject/decoder.bin
        self.get_task_names()
        self.get_tasks()
    
    def get_task_names(self):
        object_prefix = f"rawdata/{self.collection_name}/{self.name}/"
        try:
            paths = s3.list_objects_v2(Bucket='motorlearning', Prefix=object_prefix, Delimiter="/")
            self.task_names = [p.get("Prefix").split("/")[-2] for p in paths.get("CommonPrefixes")]
        except:
            raise ValueError(f"Unable to find object with prefix {object_prefix}")
    
    def get_tasks(self):
        self.tasks = {}
        for task_name in self.task_names:
            if task_name == "center_hold":
                self.tasks[task_name] = Task(self.collection_name, self.name, task_name)

    def get_decoder(self):
        # load subject's decoder and store in memory as numpy array 
        # decoders are 6x64 dimensional
        # decoder_object_name = f"metadata/{self.collection_name}/{self.subject_name}/decoder.bin"
        # decoder_object = s3.get_object(Bucket='motorlearning', Key=decoder_object_name)
        # binblob = decoder_object["Body"].read()
        # self.decoder = np.frombuffer(binblob, dtype='<f4').reshape(-1,64)
        pass

class Task():
    def __init__(self, collection_name, subject_name, task_name) -> None:
        self.collection_name = collection_name
        self.subject_name = subject_name
        self.name = task_name
        self.get_session_names()
        self.get_sessions()

    def get_session_names(self):
        object_prefix = f"rawdata/{self.collection_name}/{self.subject_name}/{self.name}/"
        try:
            paths = s3.list_objects_v2(Bucket='motorlearning', Prefix=object_prefix, Delimiter="/")
            self.session_names = [p.get("Prefix").split("/")[-2] for p in paths.get("CommonPrefixes")]
        except:
            raise ValueError(f"Unable to find object with prefix {object_prefix}")

    def get_sessions(self):
        self.sessions = {}        
        for session_name in self.session_names:
            session_number = int(session_name.split("_")[-1])
            # exceptions for the center hold dataset
            if self.name == "center_hold":
                # no sessions past 45
                if session_number <= 44:
                    # svenja's session numbering is +1 (1,2,3 .. 45)
                    # hyewon's first session was ended early, so we skip it
                    # andrei's session_11 is empty, so we skip it by going one higher than 11
                    if self.subject_name == "svenja" or \
                    self.subject_name == "hyewon" or \
                    (self.subject_name == "andrei" and session_number >= 11):
                        self.sessions[session_name] = Session(self.collection_name, self.subject_name, self.name, f"session_{session_number+1}")
                    else:
                        self.sessions[session_name] = Session(self.collection_name, self.subject_name, self.name, f"session_{session_number}")

    def sorted_sessions(self):
        return sorted(list(self.sessions.values()),key= lambda s: s.number)

class Session():
    def __init__(self, collection_name, subject_name, task_name, session_name) -> None:
        self.collection_name = collection_name
        self.subject_name = subject_name
        self.task_name = task_name
        self.name = session_name
        self.number = int(session_name.split("_")[-1])
        self.outcome_counts = {}
        self.trial_names = []
        self.trials = {} # named with ordinals trial_0, trial_1, ...
        self.get_outcome_array()
        self.parse_outcomes_into_trials()

    def get_outcome_array(self):
        '''
            get the behavior file for the session
            use this to generate trial names
            if the outcome is No Hold the trial number will be the same
            record the nominal trial number and the recorded trial number
        '''
        try:
            self.outcome_array.shape
        except AttributeError:
            self.outcome_array = np.ndarray([])
        # if data is there, return
        else:
            return
        # pull session behavior data from s3
        object_prefix = f"rawdata/{self.collection_name}/{self.subject_name}/{self.task_name}/{self.name}/session_result_"    
        try:
            object_key = s3.list_objects(Bucket='motorlearning', Prefix=object_prefix)["Contents"][0]["Key"]
        except:
            print(f"Unable to find object with name {self.subject_name} and prefix {object_prefix}.")
            return None
        try:
            blob = s3.get_object(Bucket='motorlearning', Key=object_key)["Body"].read()
        except:
            print(f"Unable to find object with key {object_key}.")
            return None
        self.outcome_array = np.genfromtxt(StringIO(blob.decode('utf-8')), delimiter=',', skip_header=1, dtype=None, encoding=None)
        if self.outcome_array.size == 0:
            print(f"the file with key {object_key} is empty!")

    def parse_outcomes_into_trials(self):
        for trial_idx, line in enumerate(self.outcome_array):
            trial_name = f"trial_{str(trial_idx)}"
            self.trial_names.append(trial_name)
            trial = Trial(self.collection_name, self.subject_name, self.task_name, self.name, trial_name)
            trial.set_number(trial_idx)
            trial.set_outcome(line[0])
            trial.set_target_coords([line[-2],line[-1]])
            # first trial sync up the numbers
            if trial_idx == 0:
                target_coords = [0,0]
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
            target_coords = [line[-2],line[-1]]
            trial.set_hold_time(line[1])
            if trial.outcome == "Hit":
                trial.set_reach_time(line[2])
            else:
                trial.set_reach_time(None)
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
        return sorted(list(self.trials.values()),key= lambda t: t.number)
        

class Trial():
    def __init__(self, collection_name, subject_name, task_name, session_name, trial_name) -> None:
        self.collection_name = collection_name
        self.subject_name = subject_name
        self.task_name = task_name
        self.session_name = session_name
        self.name = trial_name # trial_0: str
        self.number = None # 0: int
        self.recorded_number = None # 0: int
        self.outcome = None # "No Hold"
        self.trajectory_filename = None # XXXX.bin
        self.trajectory = None # ndarray
        self.emg_filename = None # XXXX.bin

    def set_outcome(self, outcome):
        self.outcome = outcome

    def set_target_coords(self, target_coords):
        self.target_coords = target_coords

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

    def set_trajectory_filename(self):
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

    def set_trajectory(self):
        # get task space trajectory for a given experiment, subject, task, session, trial
        # time [sec], x, y [screen coords]
        try:
            blob = s3.get_object(Bucket='motorlearning', Key=self.trajectory_filename)["Body"].read()
        except:
            raise ValueError(f"Unable to find object with prefix {self.trajectory_filename}")
        self.trajectory = np.genfromtxt(StringIO(blob.decode('utf-8')), delimiter=',', skip_header=1, dtype=float, usecols=(1,2,3), encoding=None)

    # def set_emg_filename(self, emg_filename):
    #     self.emg_filename = emg_filename

    # def get_emg(self, emg):
    #     self.emg = emg

    # def set_emg(self, emg):
    #     self.emg = emg

    # def set_filtered_emg_filename(self, filtered_emg_filename):
    #     self.filtered_emg_filename = filtered_emg_filename

    # def set_filtered_emg(self, filtered_emg):
    #     self.filtered_emg = filtered_emg

    # def get_raw_emg_file(self, collection_name: str, task_name:str, session_num: str, trial_num: str) -> np.array:
    #     """
    #         load subject's raw (unfiltered) EMG 
    #         from a particular collection, experiment, trial 
    #         and store in memory as numpy array
    #         data is num_samples X 68 dimensional
    #         last four dimensions are from recording device
    #         and include a counter channel to show dropped samples
    #     """
    #     emg_object_name = f"rawdata/{collection_name}/{self.name}/{task_name}/session_{session_num}/{trial_num}_emg_2021"
    #     matching_emg_objects = s3.list_objects(Bucket='motorlearning', Prefix=emg_object_name)
    #     if len(matching_emg_objects["Contents"]) > 1:
    #         raise ValueError(f"More than one object found with prefix {emg_object_name}")
    #     emg_object_name = matching_emg_objects["Contents"][0]["Key"]
    #     emg_object = s3.get_object(Bucket="motorlearning", Key=emg_object_name)
    #     binblob = emg_object["Body"].read()
    #     return np.frombuffer(binblob, dtype='<f4').reshape(-1,68)

    # def get_filtered_emg_file(self, collection_name: str, task_name:str, session_num: str, trial_num: str) -> np.array:
    #     """
    #         load subject's filtered EMG 
    #         from a particular collection, experiment, trial 
    #         and store in memory as numpy array
    #         data is num_samples X 64 dimensional
    #     """
    #     emg_object_name = f"rawdata/{collection_name}/{self.name}/{task_name}/session_{session_num}/{trial_num}_emg_filtered"
    #     matching_emg_objects = s3.list_objects(Bucket='motorlearning', Prefix=emg_object_name)
    #     if len(matching_emg_objects["Contents"]) > 1:
    #         raise ValueError(f"More than one object found with prefix {emg_object_name}")
    #     emg_object_name = matching_emg_objects["Contents"][0]["Key"]
    #     emg_object = s3.get_object(Bucket="motorlearning", Key=emg_object_name)
    #     binblob = emg_object["Body"].read()
    #     return np.frombuffer(binblob, dtype='<f4').reshape(-1,64)
