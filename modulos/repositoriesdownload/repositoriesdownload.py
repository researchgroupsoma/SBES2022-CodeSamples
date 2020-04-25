import os
from git import Repo


def repositoriesdownload(framework, projects):
    print('framework: ' + framework)
    with open(projects) as samples:
        for sample in samples:
            sample = remove_especial_caracters(sample)
            git_url = criate_url_from_github(sample)
            print("Downloading %s" % sample)
            repo_dir = "repositories/" + sample
            isdir = os.path.isdir(repo_dir)
            if isdir:
                print("Project " + sample + " downloaded")
                continue
            download(git_url, repo_dir, sample)
            print("%s downloaded" % sample)


def download(git_url, repo_dir, sample):
    Repo.clone_from(git_url, repo_dir + sample)


def criate_url_from_github(sample):
    return "https://github.com/" + sample + ".git"


def remove_especial_caracters(sample):
    return sample.replace('\n', '')
