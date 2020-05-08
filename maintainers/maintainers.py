from github import Github


def get_contributors(repository, githubtoken):
    g = Github(githubtoken)
    repo = g.get_repo(repository)
    contributors = repo.get_contributors()
    return contributors


def get_repository_name(framework):
    if framework == "spring":
        return "spring-projects/spring-boot"
    elif framework == "android":
        return "aosp-mirror/platform_frameworks_base"


def remove_next_line(sample):
    return sample.replace('\n', '')


def get_commom_contributors(framework_contributors, sample_contributors):
    commom = set()
    for framework_contributor in framework_contributors:
        for sample_contributor in sample_contributors:
            if framework_contributor.login == sample_contributor.login or framework_contributor.name == sample_contributor.name or framework_contributor.email == sample_contributor.email:
                commom.add(sample_contributor)
    return commom


def output_write(framework, text):
    with open("maintainers/" + framework + "_maintainers_output.csv", "a") as f:
        f.write(text + "\n")
        f.close()


def create_output(framework, path, framework_contributors, sample_contributors, commmom_contributors):
    return framework + "," + path + "," + str(framework_contributors.totalCount) + "," + str(sample_contributors.totalCount) + "," + str(len(commmom_contributors)) + "," + str(len(commmom_contributors) / framework_contributors.totalCount) + "," + str(len(commmom_contributors) / sample_contributors.totalCount)


def mainteiners(framework, projects, githubtoken):
    output_write(framework, "framework,path,framework_contributors,sample_contributors,commom_contributors,commom/framework,commom/sample")
    framework_repository = get_repository_name(framework)
    framework_contributors = get_contributors(framework_repository, githubtoken)
    with open(projects) as samples:
        for sample in samples:
            sample = remove_next_line(sample)
            sample_contributors = get_contributors(sample, githubtoken)
            commmom_contributors = get_commom_contributors(framework_contributors, sample_contributors)
            output_write(framework, create_output(framework, sample, framework_contributors, sample_contributors, commmom_contributors))
