from utils import get_py_github_instance, output_write, get_samples


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


def file_extension_changes(framework, projects, githubtoken):
    samples = get_samples(projects)
    g = get_py_github_instance(githubtoken)
    for sample in samples:
        configuration_files = create_configuration_dict()
        extension_files = create_extension_dict()
        r = g.get_repo(sample)
        commits = r.get_commits()
        for commit in commits:
            for file in commit.files:
                filename = get_file_name(file.filename)
                calculate_configuration_files(configuration_files, filename)
                calculate_extension_files(filename, extension_files)
        write_header(configuration_files, extension_files, framework, "file_extension_changes")
        write_content(configuration_files, extension_files, framework, sample, "file_extension_changes")


def file_extension_changes_forks(framework, projects, githubtoken):
    samples = get_samples(projects)
    g = get_py_github_instance(githubtoken)
    for sample in samples:
        configuration_files = create_configuration_dict()
        extension_files = create_extension_dict()
        r = g.get_repo(sample)
        forks = r.get_forks()
        for fork in forks:
            comparation = r.compare(r.default_branch, fork.owner.login + ":" + fork.default_branch)
            commits = comparation.commits
            for commit in commits:
                for file in commit.files:
                    filename = get_file_name(file.filename)
                    calculate_configuration_files(configuration_files, filename)
                    calculate_extension_files(filename, extension_files)
            write_header(configuration_files, extension_files, framework, "file_extension_changes_forks")
            write_content(configuration_files, extension_files, framework, fork.full_name, "file_extension_changes_forks")
