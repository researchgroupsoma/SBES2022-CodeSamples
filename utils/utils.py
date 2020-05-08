import fnmatch
import os


def remove_next_line(sample):
    return sample.replace('\n', '')


def output_write(framework, measure, text, clean):
    if clean:
        with open(measure + "/" + framework + "_" + measure + "_output.csv", "w") as f:
            f.close()
    with open(measure + "/" + framework + "_" + measure + "_output.csv", "a") as f:
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
