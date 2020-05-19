from utils import get_py_github_instance, output_write, get_samples
from utils.utils import manage_limit_rate, print_status_samples, remove_next_line
from git import Repo
import subprocess


def get_file_name(filename):
    return filename.split("/")[-1]


def get_file_extension(filename):
    try:
        return filename.split(".")[1]
    except:
        return filename


def create_extension_dict():
    return {"java": 0, "properties": 0, "jar": 0, "xml": 0, "bat": 0, "md": 0, "adoc": 0, "yaml": 0, "txt": 0, "sh": 0, "yml": 0, "cmd": 0, "kt": 0, "json": 0, "others": 0}


def create_configuration_dict():
    return {"build.gradle": 0, "pom.xml": 0, "travis.yml": 0, "AndroidManifest.xml": 0, "readme.md": 0}


def calculate_configuration_files(configuration_files, filename):
    for configuration_file in configuration_files:
        if configuration_file == filename:
            configuration_files[configuration_file] += 1


def calculate_extension_files(extensions, filename):
    extension_file = get_file_extension(filename)
    try:
        extensions[extension_file] += 1
    except:
        extensions["others"] += 1


def write_content(action_in_files, configuration_files, extension_files, framework, sample, measure):
    output = framework + "," + sample
    actions_count = 0
    for action in action_in_files:
        output += "," + str(action_in_files[action])
        actions_count += action_in_files[action]
    output += "," + str(actions_count)
    for file in extension_files:
        output += "," + str(extension_files[file])
    for file in configuration_files:
        output += "," + str(configuration_files[file])
    output_write(framework, "file_extension_changes", measure, output, False)


def write_header(action_in_files, configuration_files, extension_files, framework, measure):
    output = "framework,path"
    for action in action_in_files:
        output += "," + action
    output += ",total_actions"
    for file in extension_files:
        output += "," + file
    for file in configuration_files:
        output += "," + file
    output_write(framework, "file_extension_changes", measure, output, True)


def create_output_directory(owner):
    subprocess.call(["bash", "-c", "mkdir -p file_extension_changes/"+owner])


def extract_changes_log(directory, sample):
    repositories_path = "repositories/"
    create_output_directory(sample.split("/")[0])
    output_directory = directory + "/" + sample + ".txt"
    sample_path = repositories_path + sample
    sample_repository = Repo(repositories_path + sample)
    active_branch = sample_repository.active_branch
    git_checkout(active_branch, sample_path)
    subprocess.call(["bash", "-c",
                     "git -C {0} log --name-status --stat --pretty=format:'%h;%s' > {1}".format(sample_path,
                                                                                                output_directory)])


def git_checkout(active_branch, sample_path):
    subprocess.call(["bash", "-c", "git -C {0} checkout -f {1}".format(sample_path, active_branch)])


def file_extension_changes_forks(framework, projects, githubtoken):
    samples = get_samples(projects)
    g = get_py_github_instance(githubtoken)
    configuration_files = create_configuration_dict()
    extension_files = create_extension_dict()
    write_header(configuration_files, extension_files, framework, "file_extension_changes_forks")
    for i, sample in enumerate(samples):
        configuration_files = create_configuration_dict()
        extension_files = create_extension_dict()
        manage_limit_rate(len(samples))
        print_status_samples(i, len(samples))
        r = g.get_repo(sample)
        forks = r.get_forks()
        for f, fork in enumerate(forks):
            manage_limit_rate(forks.totalCount)
            print("{0}% forks completed from sample {1}".format(((f+1)/forks.totalCount), sample))
            try:
                comparation = r.compare(r.default_branch, fork.owner.login + ":" + fork.default_branch)
                if comparation.ahead_by < 1:
                    continue
            except:
                continue
            commits = comparation.commits
            for commit in commits:
                manage_limit_rate(len(commits))
                for file in commit.files:
                    manage_limit_rate(len(commit.files))
                    filename = get_file_name(file.filename)
                    calculate_configuration_files(configuration_files, filename)
                    calculate_extension_files(filename, extension_files)
            write_content(configuration_files, extension_files, framework, fork.full_name, "file_extension_changes_forks")


def file_extension_changes(framework, projects):
    print("Computing file extension changes")
    samples = get_samples(projects)
    configuration_files = create_configuration_dict()
    extension_files = create_extension_dict()
    action_in_files = {"A": 0, "M": 0, "D": 0}
    write_header(action_in_files, configuration_files, extension_files, framework, "file_extension_changes")
    for sample in samples:
        extract_changes_log("file_extension_changes", sample)
        configuration_files = create_configuration_dict()
        extension_files = create_extension_dict()
        action_in_files = {"A": 0, "M": 0, "D": 0}
        with open("file_extension_changes/"+sample+".txt") as logs:
            for log in logs:
                log = remove_next_line(log)
                if ";" not in log:
                    if ("A" in log) or ("M" in log) or ("D" in log):
                        try:
                            log = log.split("\t")
                            action = log[0]
                            file = get_file_name(log[1])
                            calculate_configuration_files(configuration_files, file)
                            calculate_extension_files(extension_files, file)
                            action_in_files[action] += 1
                        except:
                            continue
        write_content(action_in_files, configuration_files, extension_files, framework, sample, "file_extension_changes")