from github import Github, GithubException
import datetime


def remove_next_line(sample):
    return sample.replace('\n', '')


def output_write(framework, text):
    with open("githubmetadata/" + framework + "_metadata_output.csv", "a") as f:
        f.write(text + "\n")
        f.close()


def get_projects_count(repo):
    try:
        projects_count = repo.get_projects().totalCount
        return projects_count
    except GithubException:
        return None


def get_update_at(repo):
    return repo.updated_at


def get_opened_pull_requests_count(repo):
    return repo.get_pulls().totalCount


def get_closed_pull_requests_count(repo):
    return repo.get_pulls(state="closed").totalCount


def get_watchers_count(repo):
    return repo.watchers


def get_commits_count(repo):
    return repo.get_commits().totalCount


def get_forks_count(repo):
    return repo.forks


def get_opened_issues_count(repo):
    return repo.get_issues(state="open").totalCount


def get_closed_issues_count(repo):
    return repo.get_issues(state="closed").totalCount


def get_stars_count(repo):
    return repo.stargazers_count


def get_lifetime(repo):
    first_commit = repo.get_commits().reversed[0]
    first_commit_date = first_commit.commit.author.date
    now = datetime.datetime.now()
    lifetime = now - first_commit_date
    return lifetime.days


def get_lifetime_per_commit(repo):
    lifetime = get_lifetime(repo)
    commits_count = get_commits_count(repo)
    lifetime_per_commit = lifetime / commits_count
    return lifetime_per_commit


def build_output(framework, repo, sample):
    return framework + "," + sample + "," + str(get_forks_count(repo)) + "," + str(get_stars_count(repo)) + "," + \
           str(get_watchers_count(repo)) + "," + str(get_opened_issues_count(repo)) + "," + \
           str(get_closed_issues_count(repo)) + "," + str(get_commits_count(repo)) + "," + \
           str(get_opened_pull_requests_count(repo)) + "," + str(get_closed_pull_requests_count(repo)) + "," + \
           str(get_update_at(repo)) + "," + str(get_projects_count(repo)) + "," + str(get_lifetime(repo)) + "," + \
           str(get_lifetime_per_commit(repo))


def githubmetadata(framework, projects, githubtoken):
    output_write(framework,
                 "framework,repository,forks,stargazers,watchers,openedIssues,closedIssues,commits,"
                 "openedPullRequests,closedPullRequests,updatedAt,projects,lifetime,lifetime per commit")
    g = Github(githubtoken)
    with open(projects) as samples:
        for sample in samples:
            sample = remove_next_line(sample)
            repo = g.get_repo(sample)
            output = build_output(framework, repo, sample)
            output_write(framework, output)
