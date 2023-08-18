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


class Collection():
    def __init__(self) -> None:
        self.name = None
        self.subjects = []

class Subject():
    def __init__(self, name) -> None:
        self.name = name
        self.decoder = None
        self.behavior = {}
    
    def get_decoder(self, collection_name: str):
        """
        load subject's decoder and store in memory as numpy array 
        decoders are 6x64 dimensional
        """
        decoder_object_name = f"metadata/{collection_name}/{self.name}/decoder.bin"
        decoder_object = s3.get_object(Bucket='motorlearning', Key=decoder_object_name)
        binblob = decoder_object["Body"].read()
        self.decoder = np.frombuffer(binblob, dtype='<f4').reshape(-1,64)

    def get_center_hold_trajectory(self, collection_name, subject_name, session_num, trial_num):
        # get task space trajectory for a given experiment, subject, task, session, trial
        # time [sec], x, y [screen coords]
        object_prefix = f"rawdata/{collection_name}/{subject_name}/center_hold/session_{session_num}/{trial_num}_behavior_"
        try:
            object_key = s3.list_objects(Bucket='motorlearning', Prefix=object_prefix)["Contents"][0]["Key"]
        except:
            raise ValueError(f"Unable to find object with prefix {object_prefix}")
        blob = s3.get_object(Bucket='motorlearning', Key=object_key)["Body"].read()
        return np.genfromtxt(StringIO(blob.decode('utf-8')), delimiter=',', skip_header=1, dtype=float, usecols=(1,2,3), encoding=None)

    def get_center_hold_outcomes(self, collection_name):
        self.outcomes = {}
        for session_num in range(45):
            hits, misses, noholds, outcomes = self.get_session_outcomes(collection_name, str(session_num))
            self.outcomes[str(session_num)] = {}
            self.outcomes[str(session_num)]["outcomes"] = outcomes
            self.outcomes[str(session_num)]["hits"] = hits
            self.outcomes[str(session_num)]["misses"] = misses
            self.outcomes[str(session_num)]["noholds"] = noholds
            self.outcomes[str(session_num)]["hit_percentage"] = analysis.calculate_hit_percentage(hits)

    def get_raw_emg_file(self, collection_name: str, task_name:str, session_num: str, trial_num: str) -> np.array:
        """
            load subject's raw (unfiltered) EMG 
            from a particular collection, experiment, trial 
            and store in memory as numpy array
            data is num_samples X 68 dimensional
            last four dimensions are from recording device
            and include a counter channel to show dropped samples
        """
        emg_object_name = f"rawdata/{collection_name}/{self.name}/{task_name}/session_{session_num}/{trial_num}_emg_2021"
        matching_emg_objects = s3.list_objects(Bucket='motorlearning', Prefix=emg_object_name)
        if len(matching_emg_objects["Contents"]) > 1:
            raise ValueError(f"More than one object found with prefix {emg_object_name}")
        emg_object_name = matching_emg_objects["Contents"][0]["Key"]
        emg_object = s3.get_object(Bucket="motorlearning", Key=emg_object_name)
        binblob = emg_object["Body"].read()
        return np.frombuffer(binblob, dtype='<f4').reshape(-1,68)

    def get_filtered_emg_file(self, collection_name: str, task_name:str, session_num: str, trial_num: str) -> np.array:
        """
            load subject's filtered EMG 
            from a particular collection, experiment, trial 
            and store in memory as numpy array
            data is num_samples X 64 dimensional
        """
        emg_object_name = f"rawdata/{collection_name}/{self.name}/{task_name}/session_{session_num}/{trial_num}_emg_filtered"
        matching_emg_objects = s3.list_objects(Bucket='motorlearning', Prefix=emg_object_name)
        if len(matching_emg_objects["Contents"]) > 1:
            raise ValueError(f"More than one object found with prefix {emg_object_name}")
        emg_object_name = matching_emg_objects["Contents"][0]["Key"]
        emg_object = s3.get_object(Bucket="motorlearning", Key=emg_object_name)
        binblob = emg_object["Body"].read()
        return np.frombuffer(binblob, dtype='<f4').reshape(-1,64)

    def get_session_behavior(self, collection_name, session_num):
        session_num_str = str(session_num)
        # see if the data is already in the subject
        try:
            self.behavior[collection_name] 
        except KeyError:
            self.behavior[collection_name] = {}
            print(f"created {collection_name} for {self.name}")
        # if data is there, return
        try:
            self.behavior[collection_name][session_num_str]
        except KeyError:
            pass
        else:
            # return early if the dict is there
            return
        # pull session behavior data from s3
        # make a dumb exception for svenja, whose session numbering is +1 (1,2,3 .. 45)
        # hyewon's first session was ended early, so we skip it
        if self.name == "svenja" or self.name == "hyewon":
            object_prefix = f"rawdata/{collection_name}/{self.name}/center_hold/session_{session_num+1}/session_result_"
        else:
            object_prefix = f"rawdata/{collection_name}/{self.name}/center_hold/session_{session_num}/session_result_"
        try:
            object_key = s3.list_objects(Bucket='motorlearning', Prefix=object_prefix)["Contents"][0]["Key"]
        except:
            print(f"Unable to find object with name {self.name} and prefix {object_prefix}.")
            return None
        try:
            blob = s3.get_object(Bucket='motorlearning', Key=object_key)["Body"].read()
        except:
            print(f"Unable to find object with key {object_key}.")
            return None
        self.behavior[collection_name][session_num_str] = np.genfromtxt(StringIO(blob.decode('utf-8')), delimiter=',', skip_header=1, dtype=None, encoding=None)

    def get_session_outcomes(self, collection_name, session_num):
        # make a dict to hold outcomes over trials
        self.get_session_behavior(collection_name, session_num)
        outcomes = {}
        for trial_idx, line in enumerate(self.behavior[collection_name][str(session_num)]):
            outcomes[f"trial_{str(trial_idx)}"] = {} 
            outcomes[f"trial_{str(trial_idx)}"]["outcome"] = line[0]
            outcomes[f"trial_{str(trial_idx)}"]["target"] = [line[-2],line[-1]]
            outcomes[f"trial_{str(trial_idx)}"]["hold_time"] = line[1]
            if line[0] == "Hit":
                outcomes[f"trial_{str(trial_idx)}"]["reach_time"] = line[2]
            else:
                outcomes[f"trial_{str(trial_idx)}"]["reach_time"] = None
        return outcomes
    
    def get_session_outcome_counts(self, collection_name, session_num):
        # get count totals for outcomes for the session-- hits, misses, noholds
        self.get_session_behavior(collection_name, session_num)
        outcomes = [line[0] for line in self.behavior[collection_name][str(session_num)]]
        # count unique outcomes
        uniques, counts = np.unique(outcomes, return_counts=True)
        outcome_counts = {}
        for outcome, count in zip(uniques, counts):
            if outcome == "Hit":
                outcome_counts["hits"] = count
            elif outcome == "Miss":
                outcome_counts["misses"] = count
            elif outcome == "No Hold":
                outcome_counts["noholds"] = count
            else:
                raise ValueError("Unforeseen outcome in behavior: ", outcome)
        # if outcome didn't happen, put a 0
        if "Hit" not in outcomes:
            outcome_counts["hits"] = 0
        if "Miss" not in outcomes:
            outcome_counts["misses"] = 0
        if "No Hold" not in outcomes:
            outcome_counts["noholds"] = 0
        return outcome_counts
        