import numpy as np
from analysis import files
import matplotlib.pyplot as plt
from matplotlib.markers import MarkerStyle


def log(x, a, b):
    return b * np.log(x) + a

def calculate_hit_percentage(num_hits):
    num_targets = 12
    return 100 * num_hits / num_targets

def get_outcomes(experiment, subject):
    session_path_list = files.get_session_path_list(experiment, subject)
    num_sessions = len(session_path_list)
    hits = []
    misses = []
    noholds = []
    reach_times = []
    for behavior_path in session_path_list:
        outcome_path = [x for x in behavior_path.iterdir() if "result" in x.name][0]
        behavior = np.genfromtxt(
            str(outcome_path), delimiter=",", skip_header=1, dtype=None, encoding=None
        )
        outcomes = [x[0] for x in behavior]
        for x in behavior:
            if x[0] == "Hit":
                reach_times.append(x[2])
            elif x[0] == "Miss":
                reach_times.append(x[2])
            else:
                reach_times.append(np.inf)
        uniques, counts = np.unique(outcomes, return_counts=True)
        for outcome, count in zip(uniques, counts):
            if outcome == "Hit":
                hits.append(count)
            elif outcome == "Miss":
                misses.append(count)
            elif outcome == "No Hold":
                noholds.append(count)
            else:
                raise ValueError("Unforeseen outcome in behavior: ", outcome)
        if "Hit" not in outcomes:
            hits.append(0)
        if "Miss" not in outcomes:
            misses.append(0)
        if "No Hold" not in outcomes:
            noholds.append(0)
    return hits, misses, noholds, num_sessions, reach_times


def plot_hit_curves(experiment, subjects, subjects_to_plot=[], ax=None):
    stats = []
    hf = []
    if ax is None:
        fig, ax = plt.subplots(1, 1, figsize=(24, 8))
    for subject in subjects:
        hits, misses, noholds, num_sessions = get_outcomes(experiment, subject)
        fractions = [h * (100 / 12) for h in hits]
        sessions_idxs = range(len(fractions))
        # x = np.linspace(0, num_sessions, 50)
        # popt, pcov = curve_fit(log, list(range(1, num_sessions + 1)), fractions)
        total_fraction = 100 * sum(hits) / (num_sessions * 12)
        # rate = popt[1]
        stats.append(
            f"{subject}: \n Hit Fraction: {round(total_fraction,1)}% \n"
        )  # \n Baseline: {round(popt[0],1)}% \n Rate: {round(rate,1)} \n")
        hf.append(total_fraction)
        if subject in subjects_to_plot:
            ax.plot(fractions, "-o", label=subject, zorder=10)
            # plt.plot(x, log(x, *popt), "k--", zorder=10)
        else:
            ax.plot(fractions, "-o", color="gray", alpha=0.3)
            # plt.plot(x, log(x, *popt), "k--", alpha=0.3)
    ax.set_xlabel("block")
    ax.set_ylabel("hit fraction")
    ax.set_title("hit fractions over sessions")
    ax.set_ylim([0, 100])
    ax.set_xticks(range(num_sessions))
    ax.set_xticklabels(range(1, num_sessions + 1))
    ax.grid(True, which="major")
    ax.legend()
    return ax, hf, stats

def plot_circle(x,y,r,ax,style="k"):
    theta = np.linspace(0, 2*np.pi, 100)
    ax.plot(r*np.cos(theta)+x, r*np.sin(theta)+y,style)
    
def plot_targets(ax,style="ko",markersize=5, target=None):
    m = MarkerStyle("o", fillstyle="none")
    theta = np.linspace(0, 2*np.pi, 13) + np.pi
    ax.plot(np.cos(theta), np.sin(theta), style, marker=m, markersize=markersize, color="grey")
    if not target is None: 
        ax.plot(target[0], target[1], "ro", markersize=markersize)
    
    
def plot_box(ax):
    ax.plot(0,0,'ks',zorder=20)
    plot_circle(0,0,.15,ax)
    ax.plot([-1,1],[-1,-1],"k")
    ax.plot([-1,1],[1,1],"k")
    ax.plot([1,1],[-1,1],"k")
    ax.plot([-1,-1],[-1,1],"k")
    
def plot_control_preview(data, decoder, ax, label=""):
    ax.plot(np.dot(decoder[-1:],data.T)[0],np.dot(decoder[-2:-1],data.T)[0],label=label)
    ax.plot(np.dot(decoder[-1:],data.T)[0].mean(),np.dot(decoder[-2:-1],data.T)[0].mean(),"o",label=label+"mean",zorder=10)

def plot_dynamics_preview(data, dynamics, decoder, label=""):
    fig, ax = plt.subplots(1,1)
    states = []
    state = np.zeros(shape=(6,1))
    for sample in data:
        state = utils.advance_dynamics(dynamics,state,decoder,sample.reshape(-1,1))
        states.append(state)
    states = np.hstack(states)
    ax.set_ylim([-2,2])
    ax.set_xlim([-2,2])
    plot_box(ax)
    # plot_control_preview(offset_movement_data, decoder, ax)
    ax.plot(states[0],states[1])
    ax.plot(states[0].mean(),states[1].mean(),"ro")
    ax.legend()
    return states


def get_task_paths(subject_folder):
    task_paths = {}
    for x in subject_folder.iterdir(): 
        if x.name[0] != ".":
            task_paths[x.name] = x
    return task_paths

def get_outcome_path(block_path):
    return [x for x in block_path.iterdir() if "result" in x.name][0]

# behavior space trajectories
def load_behavior(path):
    return np.genfromtxt(path, delimiter=',', skip_header=1, dtype=float, encoding=None)

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


class Subject():
    def __init__(self):
        self.sessions = []


class Trial():
    def __init__(self):
        self.target_coordinate = None
        self.outcome = None
        self.hold_time = None
        self.reach_time = None
        
        self.idx = None
        self.target_idx = None
        self.session = None
        self.behavior_path = None
        self.emg_path = None
        
    def parse_outcome(self, outcome):
        self.target_coordinate = outcome["target"]
        self.outcome = outcome["outcome"]
        self.hold_time = outcome["hold_time"]
        self.reach_time = outcome["reach_time"]

    def parse_target(self, coord):
        for idx, t in enumerate(self.targets):
            if sum(abs(coord - t)) < 0.001:
                return idx

class Session():
    def __init__(self, path):
        self.path = path
        self.outcomes = self.get_outcomes()
        self.trials = self.add_trials()
        self.idx = int(path.name.split("_")[-1])
        self.add_paths_to_trials()
        
    def get_outcomes(self):
        outcome_path = get_outcome_path(self.path)
        # get something we can index
        #  outcome, HT, RT, tX, tY
        behavior = np.genfromtxt(str(outcome_path), delimiter=',', skip_header=1, dtype=None, encoding=None)
        outcome_dict = {}
        for i, x in enumerate(behavior):
            outcome_dict[str(i)] = {}
            outcome_dict[str(i)]["outcome"] = x[0]
            outcome_dict[str(i)]["target"] = [x[-2],x[-1]]
            outcome_dict[str(i)]["hold_time"] = x[1]
            if x[0] == "Hit":
                outcome_dict[str(i)]["reach_time"] = x[2]
            else:
                outcome_dict[str(i)]["reach_time"] = None
        return outcome_dict
        
    def add_trials(self):
        trials = []
        for _, outcome in self.outcomes.items(): # trial_path, trial_outcome in b.outcomes:
            trial = Trial()
            trial.parse_outcome(outcome)
            trials.append(trial)
        return trials

    def add_paths_to_trials(self):
        emg_paths = sorted([x for x in self.path.iterdir() if "emg" in x.name and "filtered" not in x.name and x.suffix == ".bin"], key=files.parse_filename_prefix)
        filtered_paths = sorted([x for x in self.path.iterdir() if "emg" in x.name and "filtered" in x.name and x.suffix == ".bin"], key=files.parse_filename_prefix)
        behavior_paths = sorted([x for x in self.path.iterdir() if "behavior" in x.name and x.suffix == ".csv"], key=files.parse_filename_prefix)
        assert len(emg_paths) == len(self.trials), "mismatch between number of trials and number of paths"
        assert len(filtered_paths) == len(self.trials), "mismatch between number of trials and number of paths"
        assert len(behavior_paths) == len(self.trials), "mismatch between number of trials and number of paths"
        for emg_path, filtered_path, behavior_path, trial in zip(emg_paths, filtered_paths, behavior_paths, self.trials):
            trial.emg_path = emg_path
            trial.filtered_path = filtered_path
            trial.behavior_path = behavior_path
            