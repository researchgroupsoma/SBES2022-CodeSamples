from utils import get_samples, get_py_github_instance
from utils.utils import manage_limit_rate, remove_next_line, output_write
from git import Repo
import subprocess
import shutil

def get_file_name(filename):
    return filename.split("/")[-1]


def get_file_extension(filename):
    try:
        return filename.split(".")[1]
    except:
        return filename


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


def create_output_directory(owner):
    subprocess.call(["bash", "-c", "mkdir -p file_extension_changes_forks/"+owner])


def git_checkout(active_branch, sample_path):
    subprocess.call(["bash", "-c", "git -C {0} checkout -f {1}".format(sample_path, active_branch)])


def extract_changes_log(repositories_path, directory, sample, comparation):
    create_output_directory(sample.split("/")[0])
    output_directory = directory + "/" + sample + ".txt"
    sample_path = repositories_path + sample
    sample_repository = Repo(repositories_path + sample)
    active_branch = sample_repository.active_branch
    git_checkout(active_branch, sample_path)
    subprocess.call(["bash", "-c", "git -C {0} log --name-status --stat --pretty=format:'%h;%s' {1}...HEAD > {2}".format(sample_path, comparation.merge_base_commit.sha ,output_directory)])

def create_configuration_dict():
    return {"build.gradle": 0, "pom.xml": 0, "travis.yml": 0, "AndroidManifest.xml": 0, "readme.md": 0}


def create_extension_dict():
    return {"java": 0, "properties": 0, "jar": 0, "xml": 0, "bat": 0, "md": 0, "adoc": 0, "yaml": 0, "txt": 0, "sh": 0, "yml": 0, "cmd": 0, "kt": 0, "json": 0, "others": 0}


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
    output_write(framework, "file_extension_changes_forks", measure, output, False)


def write_header(action_in_files, configuration_files, extension_files, framework, measure):
    output = "framework,path"
    for action in action_in_files:
        output += "," + action
    output += ",total_actions"
    for file in extension_files:
        output += "," + file
    for file in configuration_files:
        output += "," + file
    output_write(framework, "file_extension_changes_forks", measure, output, True)


def file_extension_changes_forks(framework, projects, githubtoken):
    samples = get_samples(projects)
    g = get_py_github_instance(githubtoken)
    action_in_files = {"A": 0, "M": 0, "D": 0}
    extension_files = create_extension_dict()
    configuration_files = create_configuration_dict()
    write_header(action_in_files, configuration_files, extension_files, framework, "file_extension_changes_forks")
    for sample in samples:
        manage_limit_rate(len(samples))
        print(sample)
        repository = g.get_repo(sample)
        forks = repository.get_forks()
        for fork in forks:
            manage_limit_rate(forks.totalCount)
            try:
                comparation = repository.compare(repository.default_branch, fork.owner.login + ":" + fork.default_branch)
                if comparation.ahead_by > 0:
                    print("Downloading " + fork.full_name)
                    Repo.clone_from(fork.clone_url, "forks_repositories/"+fork.full_name)
                    print("Downloaded " + fork.full_name)
                    extract_changes_log("forks_repositories/", "file_extension_changes_forks", fork.full_name, comparation)
                    configuration_files = create_configuration_dict()
                    extension_files = create_extension_dict()
                    action_in_files = {"A": 0, "M": 0, "D": 0}
                    with open("file_extension_changes_forks/" + fork.full_name + ".txt") as logs:
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
                    write_content(action_in_files, configuration_files, extension_files, framework, fork.full_name, "file_extension_changes_forks")
                    shutil.rmtree("forks_repositories/"+fork.full_name.split("/")[0])
                    shutil.rmtree("file_extension_changes_forks/"+fork.full_name.split("/")[0])
                    print("{0} deleted".format(fork.full_name))
            except Exception:
                print(Exception)
