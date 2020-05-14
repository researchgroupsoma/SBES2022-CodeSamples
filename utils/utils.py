import fnmatch
import os
from github import Github
import time


def remove_next_line(sample):
    return sample.replace('\n', '')


def output_write(framework, directory, measure, text, clean):
    if clean:
        with open(directory + "/" + framework + "_" + measure + "_output.csv", "w") as f:
            f.close()
    with open(directory + "/" + framework + "_" + measure + "_output.csv", "a") as f:
        f.write(text + "\n")
        f.close()


def find_paths(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        if '.git' in root:
            continue
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result


def get_samples(projects):
    samples_output = []
    with open(projects) as samples:
        for sample in samples:
            sample = remove_next_line(sample)
            samples_output.append(sample)
    return samples_output


def get_py_github_instance(githubtoken):
    global g
    g = Github(githubtoken)
    return g


def manage_limit_rate():
    if g.rate_limiting[0] < 10:
        sleep_time = int((g.rate_limiting_resettime - time.time()))
        sleep_time = sleep_time * 1.05
        print("Sleeping for: " + str(sleep_time / 60) + " minutes")
        time.sleep(sleep_time)


def print_status_samples(index, size):
    print("{0}% Completed samples".format((index / size) * 100))
