from github import UnknownObjectException
from utils import get_py_github_instance, output_write, get_samples
from utils.utils import manage_limit_rate, print_status_samples


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


def calculate_extension_files(filename, extensions):
    extension_file = get_file_extension(filename)
    try:
        extensions[extension_file] += 1
    except:
        extensions["others"] += 1


def write_content(configuration_files, extension_files, framework, sample, measure):
    output = framework + "," + sample
    for file in extension_files:
        output += "," + str(extension_files[file])
    for file in configuration_files:
        output += "," + str(configuration_files[file])
    output_write(framework, "file_extension_changes", measure, output, False)


def write_header(configuration_files, extension_files, framework, measure):
    output = "framework,path"
    for file in extension_files:
        output += "," + file
    for file in configuration_files:
        output += "," + file
    output_write(framework, "file_extension_changes", measure, output, True)


def print_status_commit(commits, j, sample):
    print("{0}% Completed commits from samples {1}".format((((j + 1) / commits.totalCount) * 100), sample))


def file_extension_changes(framework, projects, githubtoken):
    print("Computing file extension changes")
    samples = get_samples(projects)
    g = get_py_github_instance(githubtoken)
    configuration_files = create_configuration_dict()
    extension_files = create_extension_dict()
    write_header(configuration_files, extension_files, framework, "file_extension_changes")
    for i, sample in enumerate(samples):
        manage_limit_rate(len(samples))
        print_status_samples(i+1, len(samples))
        r = g.get_repo(sample)
        commits = r.get_commits()
        for j, commit in enumerate(commits):
            manage_limit_rate(commits.totalCount)
            print_status_commit(commits, j, sample)
            for file in commit.files:
                manage_limit_rate(len(commit.files))
                filename = get_file_name(file.filename)
                calculate_configuration_files(configuration_files, filename)
                calculate_extension_files(filename, extension_files)
        write_content(configuration_files, extension_files, framework, sample, "file_extension_changes")


def file_extension_changes_forks(framework, projects, githubtoken):
    samples = get_samples(projects)
    g = get_py_github_instance(githubtoken)
    configuration_files = create_configuration_dict()
    extension_files = create_extension_dict()
    write_header(configuration_files, extension_files, framework, "file_extension_changes_forks")
    for i, sample in enumerate(samples):
        manage_limit_rate(len(samples))
        print_status_samples(i, samples)
        r = g.get_repo(sample)
        forks = r.get_forks()
        for f, fork in enumerate(forks):
            manage_limit_rate(forks.totalCount)
            print("{0}% forks completed from sample {1}".format(((f+1)/forks.totalCount), sample))
            try:
                comparation = r.compare(r.default_branch, fork.owner.login + ":" + fork.default_branch)
                if comparation.ahead_by < 1:
                    print("Polou o " + fork.full_name)
                    continue
            except UnknownObjectException:
                print("Deu ruim")
                continue
            commits = comparation.commits
            for commit in commits:
                manage_limit_rate(commits.totalCount)
                for file in commit.files:
                    manage_limit_rate(len(commit.files))
                    filename = get_file_name(file.filename)
                    calculate_configuration_files(configuration_files, filename)
                    calculate_extension_files(filename, extension_files)
            write_content(configuration_files, extension_files, framework, fork.full_name, "file_extension_changes_forks")
