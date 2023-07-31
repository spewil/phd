import numpy as np
import pathlib


def build_experiment_path_dict(experiment):
    data_folder = get_experiment_data_folder(experiment)
    subjects = [x.name for x in data_folder.iterdir() if x.name[0] != "."]
    path_dictionary = {"subjects": {}}
    for subject in subjects:
        subject_folder = data_folder / subject
        path_dictionary["subjects"].update({subject: {}})
        path_dictionary["subjects"][subject].update({"path": subject_folder})
        tasks = [x.name for x in subject_folder.iterdir() if x.name[0] != "."]
        path_dictionary["subjects"][subject].update({"tasks": {}})
        for task in tasks:
            path_dictionary["subjects"][subject]["tasks"].update(
                {task: {"path": subject_folder / task}}
            )
            session_paths = sorted(
                [
                    x
                    for x in (subject_folder / task).iterdir()
                    if x.name[0] != "." and "session" in x.name
                ],
                key=lambda x: x.name[-1],
            )
            session_names = [x.name for x in session_paths]
            path_dictionary["subjects"][subject]["tasks"][task].update({"sessions": {}})
            for path, session in zip(session_paths, session_names):
                path_dictionary["subjects"][subject]["tasks"][task]["sessions"].update(
                    {session: path}
                )
    return path_dictionary


def parse_filename_prefix(x):
    name = x.name
    prefix = name[:2]
    if prefix[-1] == "_":
        return int(prefix[0])
    else:
        return int(prefix)


def parse_timestamp(x):
    name = x.name
    return name[-16:]


def write_array_to_disk(a, name):
    with open(name, "wb") as file:
        file.write(a.tobytes())


def data_files(directory):
    print(f"+ {directory}")
    paths = []
    for path in sorted(directory.rglob("*.data")):
        depth = len(path.relative_to(directory).parts)
        spacer = "    " * depth
        print(f"{spacer}+ {path.name}")
        paths.append(path)
    return paths


def list_folder_names(path):
    return [e.name for e in path.iterdir() if e.is_dir()]


def list_file_names(path, ext=None):
    if ext:
        return [e.name for e in path.iterdir() if e.is_file() and e.suffix == ext]
    else:
        return [e.name for e in path.iterdir() if e.is_file()]


def list_folders(path):
    return [e for e in path.iterdir() if e.is_dir()]


def list_files(path, ext=None):
    if ext:
        return [e for e in path.iterdir() if e.is_file() and e.suffix == ext]
    else:
        return [e for e in path.iterdir() if e.is_file()]


def load_from_bin_file(path):
    if path.suffix != ".bin":
        raise AssertionError("Files must be in binary format.")
    data = np.fromfile(path, dtype=np.int32)
    num_channels = 32
    return np.array(data.reshape(-1, num_channels + 4).T, dtype=np.float)


def load_from_file(filepath, nch, dtype, order="C"):
    with open(filepath, "rb") as f:
        data = np.fromfile(f, dtype=dtype)
    return data.reshape(-1, nch).T


def tree(directory, ignore=[]):
    ignore_files = [".DS_Store"] + ignore
    print(f"+ {directory}")
    for path in sorted(directory.rglob("*")):

        if path not in ignore_files:
            depth = len(path.relative_to(directory).parts)
            spacer = "    " * depth
            print(f"{spacer}+ {path.name}")


def write_array_to_disk(a, path, overwrite=False):
    if overwrite:
        with open(path, "wb") as file:
            file.write(a.tobytes())
    else:
        if path.exists():
            raise FileExistsError
        else:
            with open(path, "wb") as file:
                file.write(a.tobytes())


def load_array_from_disk(path, dtype=np.float32):
    return np.fromfile(path, dtype=dtype)


base_data_folder = pathlib.Path("/Users/spencer/motor-control/data/")


def get_experiment_data_folder(experiment):
    experiment_data_folder = base_data_folder / "rawdata" / experiment
    assert experiment_data_folder.exists(), f"Path {experiment_data_folder} not found"
    return experiment_data_folder


def get_experiment_metadata_folder(experiment):
    experiment_data_folder = base_data_folder / "metadata" / experiment
    assert experiment_data_folder.exists(), f"Path {experiment_data_folder} not found"
    return experiment_data_folder


def get_subject_folder(
    experiment,
    subject,
):
    experiment_folder = get_experiment_metadata_folder(experiment)
    subject_folder = experiment_folder / subject
    assert subject_folder.exists(), f"Path {subject_folder} not found"
    return subject_folder


def get_experiment_metadata(experiment):
    experiment_folder = get_experiment_folder(experiment)
    with open(experiment_folder / "metadata.json", "r") as fp:
        experiment_metadata = json.load(fp)
    return experiment_metadata


def get_session_metadata(experiment, session):
    experiment_folder = get_experiment_metadata_folder(experiment)
    with open(experiment_folder / (str(session) + ".json"), "r") as fp:
        session_metadata = json.load(fp)
    return session_metadata


def get_subject_metadata(experiment, subject):
    subject_folder = get_subject_folder(experiment, subject)
    with open(subject_folder / "metadata.json", "rb") as fp:
        subject_metadata = json.load(fp)
    return subject_metadata


def get_metadata(experiment, session, subject):
    return (
        get_experiment_metadata(experiment),
        get_session_metadata(experiment, session),
        get_subject_metadata(experiment, subject),
    )


def get_session_path_list(experiment, subject):
    path_dictionary = build_experiment_path_dict(experiment)
    session_dict = path_dictionary["subjects"][subject]["tasks"]["center_hold"][
        "sessions"
    ]
    session_path_list = []

    for session in sorted(
        list(session_dict.keys()), key=lambda x: int(x.split("_")[-1])
    ):
        session_path_list.append(session_dict[session])
    return session_path_list


def get_subjects(experiment, removed=None, ignored=[".DS_Store"]):
    folder = get_experiment_data_folder(experiment)
    if removed is None:
        return [f.name for f in folder.iterdir() if f.name not in ignored]
    else:
        return [
            f.name
            for f in folder.iterdir()
            if (f.name not in removed) or (f.name not in ignored)
        ]
