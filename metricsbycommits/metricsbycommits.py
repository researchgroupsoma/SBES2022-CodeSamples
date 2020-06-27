import os
from understandmetrics.understandmetrics import get_understand_metrics, create_output_directory
from utils import get_samples
from utils.utils import get_commits_from, output_write, checkout_to
from readability import Readability
from utils.utils import print_status_samples

def adding_commit_data(commit, metrics):
    metrics_aux = metrics[:2]
    metrics_aux.append(commit.hexsha)
    metrics_aux.append(commit.authored_datetime)
    metrics_aux += metrics[2:]
    return metrics_aux


def get_necessary_metrics(understandmetrics):
    metrics_aux = []
    metrics_aux.append(understandmetrics.framework)
    metrics_aux.append(understandmetrics.sample)
    metrics_aux.append(understandmetrics.countJavaFile)
    try:
        metrics_aux.append(understandmetrics.countLineCode/understandmetrics.countJavaFile)
    except:
        metrics_aux.append(0)
    try:
        metrics_aux.append(understandmetrics.sumCyclomaticStrict/understandmetrics.countDeclMethod)
    except:
        metrics_aux.append(0)
    return metrics_aux


def get_metrics(commit, framework, sample, sample_path, udb_path):
    metrics = get_understand_metrics(framework, sample, udb_path, sample_path)
    metrics = get_necessary_metrics(metrics)
    metrics = adding_commit_data(commit, metrics)
    r = Readability(sample)
    readability = r.getReadability()
    del r
    metrics.append(readability)
    return metrics


def delete_unused_files(sample):
    os.remove("metricsbycommits/" + sample + ".csv")
    os.remove("metricsbycommits/" + sample + ".udb")

def create_output(metrics):
    output = ""
    for metric in metrics:
        output += str(metric) + ","
    return output[:-1]


def metrics_by_commits(framework, projects):
    samples = get_samples(projects)
    for index, sample in enumerate(samples):
        print_status_samples(index+1, len(samples))
        owner = sample.split("/")[0]
        create_output_directory("metricsbycommits", owner)
        output_write(sample, "metricsbycommits", "", "framework,path,commits,date,numberOfJavaFiles,countLineCode/numberOfJavaFiles,SumCyclomaticStrict/CountDeclMethod,readability",True)
        repositories_path = "/home/gabriel/Documentos/gabrielsmenezes/pesquisamestrado/repositories/"
        sample_path = repositories_path + sample
        udb_path = "metricsbycommits/" + sample
        commits = get_commits_from(sample)
        commits.reverse()
        ########## é so rodar, esta com a hash certa para o proximo
        # for index, commit in enumerate(commits):
        #     if commit.hexsha == "dfe62cb3e72c7a9cfd759dc7411197d9a629f813":
        #         position = index
        # commits = commits[position+1:]
        for index, commit in enumerate(commits):
            checkout_to(sample, commit.hexsha)
            print("commit ======= " + commit.hexsha)
            metrics = get_metrics(commit, framework, sample, sample_path, udb_path)
            output_write(sample, "metricsbycommits", "", create_output(metrics), False)
            delete_unused_files(sample)
            print("{0}% of commits completed from sample {1}".format((index/len(commits) * 100), sample))
