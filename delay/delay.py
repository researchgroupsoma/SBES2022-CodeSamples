import datetime
import os
import xml.etree.ElementTree
from git import Repo
import re
from github import Github
from utils import remove_next_line, output_write, find_paths, get_samples
from utils.utils import print_status_samples


def define_arquivo_de_configuracao(framework):
    if framework == 'spring':
        return 'pom.xml'
    elif framework == 'android':
        return 'build.gradle'


def get_namespace(element):
    m = re.match('\{.*\}', element.tag)
    return m.group(0) if m else ''


def buscar_versao_do_spring(caminho):
    try:
        arquivo = xml.etree.ElementTree.parse(caminho)
        namespace = get_namespace(arquivo.getroot())
        tag_versao = arquivo.find('./{0}parent/{0}version'.format(namespace)).text
        if 'SNAPSHOT' in tag_versao:
            return ''
        return tag_versao
    except:
        return ''


def buscar_versao_do_andorid(caminho):
    try:
        with open(caminho) as file:
            for line in file:
                if "compileSdkVersion" in line:
                    line = remove_next_line(line)
                    line = line.replace(" ", "")
                    line = line.replace("=", "")
                    version = line.split("compileSdkVersion")[1]
                    if version == '"android-O"' or version == "'android-O'":
                        version = "26"
                    if version == '"android-P"':
                        version = "28"
                    if version == "'android-Q'":
                        version = "29"
                    int(version)
                    return version
    except:
        return ""


def buscar_versao_do_framework(framework, caminho):
    if framework == 'spring':
        return buscar_versao_do_spring(caminho)
    elif framework == 'android':
        return buscar_versao_do_andorid(caminho)


def buscar_dados_de_lancamento_de_versoes(framework, githubtoken):
    versoes = {}
    if framework == 'spring':
        g = Github(githubtoken)
        repo = g.get_repo("spring-projects/spring-boot")
        tags = repo.get_tags()
        for tag in enumerate(tags):
            tag = tag[1]
            nome = tag.name.replace('v', '')
            commit = tag.commit
            versoes[nome] = commit.commit.author.date
    elif framework == 'android':
        versoes = {
            "19": datetime.datetime.strptime("2013-10-31 00:00:00", "%Y-%m-%d %H:%M:%S"),
            "20": datetime.datetime.strptime("2014-06-25 00:00:00", "%Y-%m-%d %H:%M:%S"),
            "21": datetime.datetime.strptime("2014-10-17 00:00:00", "%Y-%m-%d %H:%M:%S"),
            "22": datetime.datetime.strptime("2015-03-09 00:00:00", "%Y-%m-%d %H:%M:%S"),
            "23": datetime.datetime.strptime("2015-08-17 00:00:00", "%Y-%m-%d %H:%M:%S"),
            "24": datetime.datetime.strptime("2016-06-15 00:00:00", "%Y-%m-%d %H:%M:%S"),
            "25": datetime.datetime.strptime("2016-11-22 00:00:00", "%Y-%m-%d %H:%M:%S"),
            "26": datetime.datetime.strptime("2017-06-08 00:00:00", "%Y-%m-%d %H:%M:%S"),
            "27": datetime.datetime.strptime("2017-12-05 00:00:00", "%Y-%m-%d %H:%M:%S"),
            "28": datetime.datetime.strptime("2018-07-25 00:00:00", "%Y-%m-%d %H:%M:%S"),
            "29": datetime.datetime.strptime("2019-09-03 00:00:00", "%Y-%m-%d %H:%M:%S")
        }
    return versoes


def get_commits(repository):
    return list(reversed(list(repository.iter_commits())))


def calculate_delay(framework_release_date, sample_update_date):
    delay_in_days = sample_update_date - framework_release_date
    delay_in_days = delay_in_days.days
    if delay_in_days < 0:
        delay_in_days = 0
    return delay_in_days


def get_commit_date(commit):
    return datetime.datetime.fromtimestamp(commit.authored_date)


def get_first_version(framework, path, repository, reversed_commits):
    current_version = {}
    for index, commit in enumerate(reversed_commits):
        repository.git.checkout(commit, '-f')
        if os.path.exists(path):
            current_version = buscar_versao_do_framework(framework, path)
            reversed_commits = reversed_commits[index:]
            break
    return current_version, reversed_commits


def create_output(current_version, delay_in_days, framework, framework_release_date, next_version, path,
                  sample_update_date):
    return framework + "," + path + "," + current_version + "," + next_version + "," + framework_release_date.strftime(
        "%Y/%d/%m") + "," + sample_update_date.strftime("%Y/%d/%m") + "," + str(delay_in_days)


def delay(framework, projects, githubtoken):
    print("Computing delay to update")
    path_dos_repositorios = 'repositories'
    measure = "delay"
    output_write(framework, measure, measure, "framework,path,current_version,next_version,framework_release_date (YYYY-DD-MM),sample_update_date (YYYY-DD-MM) ,delay_in_days", True)
    framework_release_data = buscar_dados_de_lancamento_de_versoes(framework, githubtoken)
    configuration_file = define_arquivo_de_configuracao(framework)
    samples = get_samples(projects)
    for index, sample in enumerate(samples):
        print_status_samples(index+1, len(samples))
        sample_path = path_dos_repositorios + "/" + sample
        paths_configuration_file = find_paths(configuration_file, sample_path)
        repository = Repo(sample_path)
        reversed_commits = get_commits(repository)
        for path in paths_configuration_file:
            current_version, reversed_commits = get_first_version(framework, path, repository, reversed_commits)
            if current_version == {}:
                continue
            for commit in reversed_commits:
                repository.git.checkout(commit, '-f')
                next_version = buscar_versao_do_framework(framework, path)
                if current_version != next_version and next_version != '' and current_version != '' and current_version != None and next_version != None:
                    sample_update_date = get_commit_date(commit)
                    framework_release_date = framework_release_data[next_version]
                    delay_in_days = calculate_delay(framework_release_date, sample_update_date)
                    output_write(framework, measure, measure, create_output(current_version, delay_in_days, framework, framework_release_date, next_version, path, sample_update_date), False)
                    current_version = next_version
        repository.git.checkout('master', '-f')
