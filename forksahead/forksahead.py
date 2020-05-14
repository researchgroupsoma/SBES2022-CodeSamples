import time

from github import Github

from utils import get_samples, output_write


def manage_limit_rate(g, repository):
    if g.rate_limiting[0] < repository.forks_count:
        sleep_time = int((g.rate_limiting_resettime - time.time()))
        sleep_time = sleep_time * 1.05
        print("Sleeping for: " + str(sleep_time / 60) + " minutes")
        time.sleep(sleep_time)


def count_forks_ahead(framework, forks, repository):
    forks_ahead = 0
    for fork in forks:
        try:
            comparation = repository.compare(repository.default_branch, fork.owner.login + ":" + fork.default_branch)
            if comparation.ahead_by > 0:
                output_write(framework, "forksahead", "forks_ahead", framework+","+fork.full_name+","+str(comparation.ahead_by), False)
                forks_ahead = forks_ahead + 1
        except:
            continue
    return forks_ahead


def create_output(sample, framework, number_of_forks, forks_ahead, ratio_forks_ahead):
    return framework + "," + sample + "," + str(number_of_forks) + "," + str(forks_ahead) + "," + str(ratio_forks_ahead)


def forksahead(framework, projects, githubtoken):
    g = Github(githubtoken)
    output_write(framework, "forksahead", "forks_ahead_by_projects", "framework,path,number_of_forks,forks_ahead,ratio", True)
    output_write(framework, "forksahead", "forks_ahead", "framework,path,number_of_forks,forks_ahead,ratio", True)
    samples = get_samples(projects)
    for sample in samples:
        print(sample)
        repository = g.get_repo(sample)
        print("Rate limiting: " + str(g.rate_limiting[0]))
        manage_limit_rate(g, repository)
        forks = repository.get_forks()
        forks_ahead = count_forks_ahead(framework, forks, repository)
        number_of_forks = repository.forks_count
        ratio_forks_ahead = forks_ahead / number_of_forks
        output = create_output(sample, framework, number_of_forks, forks_ahead, ratio_forks_ahead)
        output_write(framework, "forksahead", "forks_ahead_by_projects", output, False)
