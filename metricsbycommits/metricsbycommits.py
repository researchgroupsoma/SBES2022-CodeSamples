import os
from understandmetrics.understandmetrics import get_understand_metrics, create_output_directory, create_output
from utils import get_samples
from utils.utils import get_commits_from, output_write, checkout_to


def adding_commit_data(commit, metrics):
    metrics_aux = metrics[:2]
    metrics_aux.append(commit.hexsha)
    metrics_aux.append(commit.authored_datetime)
    metrics_aux += metrics[2:]
    return metrics_aux


def get_necessary_metrics(metrics):
    metrics_aux = metrics[:2]
    metrics_aux.append(metrics[-1])
    try:
        metrics_aux.append(metrics[31]/metrics[-1])
    except:
        metrics_aux.append(0)
    try:
        metrics_aux.append(metrics[60]/metrics[22])
    except:
        metrics_aux.append(0)
    return metrics_aux


def get_metrics(commit, framework, sample, sample_path, udb_path):
    metrics = get_understand_metrics(framework, sample, udb_path, sample_path)
    metrics = get_necessary_metrics(metrics)
    metrics = adding_commit_data(commit, metrics)
    return metrics


def delete_unused_files(sample):
    os.remove("metricsbycommits/" + sample + ".csv")
    os.remove("metricsbycommits/" + sample + ".udb")


def metrics_by_commits(framework, projects):
    samples = get_samples(projects)
    for sample in samples:
        owner = sample.split("/")[0]
        create_output_directory("metricsbycommits", owner)
        output_write(sample, "metricsbycommits", "", "framework,path,commits,date,numberOfJavaFiles,countLineCode/numberOfJavaFiles,SumCyclomaticStrict/CountDeclMethod",True)
        repositories_path = "/home/gabriel/Documentos/gabrielsmenezes/pesquisamestrado/repositories/"
        sample_path = repositories_path + sample
        udb_path = "metricsbycommits/" + sample
        commits = get_commits_from(sample)
        commits.reverse()
        for commit in commits:
            checkout_to(sample, commit.hexsha)
            metrics = get_metrics(commit, framework, sample, sample_path, udb_path)
            output_write(sample, "metricsbycommits", "", create_output(metrics), False)
            delete_unused_files(sample)
