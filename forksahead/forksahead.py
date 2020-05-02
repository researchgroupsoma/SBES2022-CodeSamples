from github import Github
import time


def remove_next_line(sample):
    return sample.replace('\n', '')


def manage_limit_rate(g, repository):
    if g.rate_limiting[0] < repository.forks_count:
        sleep_time = int((g.rate_limiting_resettime - time.time()))
        print("Sleeping for: " + str(sleep_time / 60) + " minutes")
        time.sleep(sleep_time)


def output_write(framework, text, output_type):
    with open("forksahead/" + framework + output_type + ".csv", "a") as f:
        f.write(text + "\n")
        f.close()


def output_forks_by_sample_write(framework, text):
    output_write(framework, text, "_forks_ahead_by_projects_output")


def output_forks_write(framework, text):
    output_write(framework, text, "_forks_ahead_output")


def count_forks_ahead(framework, forks, repository):
    forks_ahead = 0
    for fork in forks:
        try:
            comparation = repository.compare(repository.default_branch, fork.owner.login + ":" + fork.default_branch)
            if comparation.ahead_by > 0:
                output_forks_write(framework, framework+","+fork.full_name+","+str(comparation.ahead_by))
                forks_ahead = forks_ahead + 1
        except:
            continue
    return forks_ahead


def forksahead(framework, projects):
    g = Github("4e7f552ac4b6ade859bc51befc6841e2cebc14b1")
    output_forks_by_sample_write(framework, "framework,path,number_of_forks,forks_ahead,ratio")
    output_forks_write(framework, "framework,path,commits_ahead")
    with open(projects) as samples:
        for sample in samples:
            sample = remove_next_line(sample)
            print(sample)
            repository = g.get_repo(sample)
            print("Rate limiting: " + str(g.rate_limiting[0]))
            manage_limit_rate(g, repository)
            forks = repository.get_forks()
            forks_ahead = count_forks_ahead(framework, forks, repository)
            number_of_forks = repository.forks_count
            ratio_forks_ahead = forks_ahead / number_of_forks
            output = create_output(sample, framework, number_of_forks, forks_ahead, ratio_forks_ahead)
            output_forks_by_sample_write(framework, output)


def create_output(sample, framework, number_of_forks, forks_ahead, ratio_forks_ahead):
    return framework + "," + sample + "," + str(number_of_forks) + "," + str(forks_ahead) + "," + str(ratio_forks_ahead)
