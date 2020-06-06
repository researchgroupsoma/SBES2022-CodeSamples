from utils import get_py_github_instance, output_write, find_paths, get_samples
from git import Repo
import shutil


def is_android(java_paths):
    for path in java_paths:
        with open(path) as java_file:
            try:
                for line in java_file:
                    if line.split(' ')[0] == 'import':
                        library = line.split(' ')[1]
                        library = library.split('.')
                        if library[0] == 'android':
                            return True
            except Exception as identifier:
                continue
    return False


def is_spring(java_paths):
    for path in java_paths:
        with open(path) as java_file:
            try:
                for line in java_file:
                    if line.split(' ')[0] == 'import':
                        library = line.split(' ')[1]
                        library = library.split('.')
                        if library[0] == 'org' and library[1] == 'springframework' and library[2] == 'boot':
                            return True
            except Exception as identifier:
                continue

    return False


def get_framework(repository):
    repository_path = "generalprojects/repositories/" + repository
    java_paths = find_paths('*.java', repository_path)
    android = is_android(java_paths)
    spring = is_spring(java_paths)
    if android and spring:
        framework = "Both"
    elif android:
        framework = "Android"
    elif spring:
        framework = "Spring"
    else:
        framework = "Other"
    return framework


def object_to_csv_line(project):
    output = ""
    for field in project:
        output = output + field + ","
    output = output[:-1]
    return output


def generalprojects(projects):
    samples = get_samples(projects)
    output_write("", "generalprojects", "projects", "path,stars,language,framework", False)
    for repository in samples:
        clone(repository)
        print("{0} baixado".format(repository))
        framework = get_framework(repository)
        print("{0} classificado como {1}".format(repository, framework))
        shutil.rmtree("generalprojects/repositories/" + repository.split("/")[0])
        print("{0} apagado".format(repository))
        output_write("", "generalprojects", "projects", "{0},{1}".format(repository, framework), False)


def clone(repository):
    Repo.clone_from("https://github.com/" + repository + ".git", "generalprojects/repositories/" + repository)