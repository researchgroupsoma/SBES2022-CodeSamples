from github import Github
from github.GithubException import IncompletableObject

from utils import get_samples
from utils import output_write


def get_contributors(repository, githubtoken):
    g = Github(githubtoken)
    repo = g.get_repo(repository)
    contributors = repo.get_contributors(anon="1")
    return contributors


def get_repository_name(framework):
    if framework == "spring":
        return "spring-projects/spring-boot"
    elif framework == "android":
        return "aosp-mirror/platform_frameworks_base"


def get_commom_contributors(framework_contributors, sample_contributors):
    commom = set()
    for framework_contributor in framework_contributors:
        for sample_contributor in sample_contributors:
            try:
                if framework_contributor.name == sample_contributor.name:
                    commom.add(sample_contributor)
                elif framework_contributor.login == sample_contributor.login:
                    commom.add(sample_contributor)
                elif framework_contributor.email == sample_contributor.email:
                    commom.add(sample_contributor)
            except Exception:
                continue
    return commom


def create_output(framework, path, framework_contributors, sample_contributors, commmom_contributors):
    return framework + "," + path + "," + str(framework_contributors.totalCount) + "," + str(sample_contributors.totalCount) + "," + str(len(commmom_contributors)) + "," + str(len(commmom_contributors) / framework_contributors.totalCount) + "," + str(len(commmom_contributors) / sample_contributors.totalCount)


def mainteiners(framework, projects, githubtoken):
    output_write(framework, "maintainers", "framework,path,framework_contributors,sample_contributors,commom_contributors,commom/framework,commom/sample", True)
    framework_repository = get_repository_name(framework)
    framework_contributors = get_contributors(framework_repository, githubtoken)
    framework_contributors.totalCount
    samples = get_samples(projects)
    for sample in samples:
        sample_contributors = get_contributors(sample, githubtoken)
        commmom_contributors = get_commom_contributors(framework_contributors, sample_contributors)
        output_write(framework, "maintainers", create_output(framework, sample, framework_contributors, sample_contributors, commmom_contributors), False)
