import datetime
import fnmatch
import os
import xml.etree.ElementTree
from git import Repo
import re
from github import Github


def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result


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
        arquivo = xml.etree.ElementTree.parse(caminho)
        print('passei')
        print(arquivo.getroot())
        namespace = get_namespace(arquivo.getroot())
        # tag_versao = arquivo.find('./{0}parent/{0}version'.format(namespace)).text
        # return tag_versao
    except:
        return ''


def buscar_versao_do_framework(framework, caminho):
    if framework == 'spring':
        return buscar_versao_do_spring(caminho)
    elif framework == 'android':
        return buscar_versao_do_andorid(caminho)


def buscar_dados_de_lancamento_de_versoes(framework):
    versoes = {}
    if framework == 'spring':
        g = Github('4e29ab283b107b0c09d7724da2c97391cffd1a4c')
        repo = g.get_repo("spring-projects/spring-boot")
        tags = repo.get_tags()
        for tag in enumerate(tags):
            tag = tag[1]
            nome = tag.name.replace('v', '')
            commit = tag.commit
            versoes[nome] = commit.commit.author.date
    elif framework == 'android':
        versoes = {
            "19": datetime.datetime.strptime("2013-10-31 00:00:00 +0000", "%Y-%m-%d %H:%M:%S %z"),
            "20": datetime.datetime.strptime("2014-06-25 00:00:00 +0000", "%Y-%m-%d %H:%M:%S %z"),
            "21": datetime.datetime.strptime("2014-10-17 00:00:00 +0000", "%Y-%m-%d %H:%M:%S %z"),
            "22": datetime.datetime.strptime("2015-03-09 00:00:00 +0000", "%Y-%m-%d %H:%M:%S %z"),
            "23": datetime.datetime.strptime("2015-08-17 00:00:00 +0000", "%Y-%m-%d %H:%M:%S %z"),
            "24": datetime.datetime.strptime("2016-06-15 00:00:00 +0000", "%Y-%m-%d %H:%M:%S %z"),
            "25": datetime.datetime.strptime("2016-11-22 00:00:00 +0000", "%Y-%m-%d %H:%M:%S %z"),
            "26": datetime.datetime.strptime("2017-06-08 00:00:00 +0000", "%Y-%m-%d %H:%M:%S %z"),
            "27": datetime.datetime.strptime("2017-12-05 00:00:00 +0000", "%Y-%m-%d %H:%M:%S %z"),
            "28": datetime.datetime.strptime("2018-07-25 00:00:00 +0000", "%Y-%m-%d %H:%M:%S %z"),
            "29": datetime.datetime.strptime("2019-09-03 00:00:00 +0000", "%Y-%m-%d %H:%M:%S %z")
        }
    return versoes


def main(framework, path_dos_samples, path_dos_repositorios):
    dados_de_lancamento_do_framework = buscar_dados_de_lancamento_de_versoes(framework)
    samples = open(path_dos_samples)
    arquivo_de_configuracao = define_arquivo_de_configuracao(framework)
    # para cada repositorio
    for sample in samples:
        sample = sample.replace('\n', '')
        caminho_do_repositorio_do_sample = path_dos_repositorios + "/" + sample
        # buscar os caminhos de todos os arquivos de configuração
        caminhos_dos_arquivos_de_configuracao = find(arquivo_de_configuracao, caminho_do_repositorio_do_sample)
        # buscar todos os commits do repositorio do primeiro até o ultimo
        repositorio = Repo(caminho_do_repositorio_do_sample)
        commits_ordem_reversa = list(reversed(list(repositorio.iter_commits())))
        # para cada caminho
        for caminho in caminhos_dos_arquivos_de_configuracao:
            # crio uma lista que guardará todas as versoes e a data de alteracao e o delay
            versao_atual = {}
            #       dou checkout no primeiro commit
            for index, commit in enumerate(commits_ordem_reversa):
                repositorio.git.checkout(commit, '-f')
                if os.path.exists(caminho):
                    versao_atual = buscar_versao_do_framework(framework, caminho)
                    commits_ordem_reversa = commits_ordem_reversa[index:]
                    break
            if versao_atual == {}:
                continue
            # para cada commit
            for commit in commits_ordem_reversa:
                # dou checkout no commit
                repositorio.git.checkout(commit, '-f')
                versao_posterior = buscar_versao_do_framework(framework, caminho)
                # verifico se a versao foi alterada
                if not versao_atual == versao_posterior and versao_posterior != '' and versao_atual != '':
                    delay = datetime.datetime.fromtimestamp(commit.authored_date) - dados_de_lancamento_do_framework[versao_posterior]
                    # print(framework, ",", caminho, ",", delay.days)
                    print(versao_atual, " ---> ", versao_posterior)
                    print(dados_de_lancamento_do_framework[versao_posterior], " ---> ", datetime.datetime.fromtimestamp(commit.authored_date), '  delay: ', delay)
                    versao_atual = versao_posterior
            # printo o caminho, versao , data de alteracao e o data de atualizacao do framework e delay

        repositorio.git.checkout('master', '-f')


main('spring', '/home/gabriel.menezes/Documentos/mestrado/pesquisa/modulos/listaDeSamples/springsamples.txt',
     '/home/gabriel.menezes/Documentos/mestrado/pesquisa/repositorios')

# main('android', '/home/gabriel.menezes/Documentos/mestrado/pesquisa/modulos/listaDeSamples/googlesamples.txt',
#      '/home/gabriel.menezes/Documentos/mestrado/pesquisa/repositorios')

# buscar_dados_de_lancamento_de_versoes('spring')

# ler o arquivo com o nome de todos os caminhos dos poms e gradles
# poms = open("/home/gabriel/Documentos/ic2/analiseDosProjetosGerais/RQ2/extraindoVersaoAtualDoFramework/Spring.csv")
# gradles = open("/home/gabriel/Documentos/ic2/analiseDosProjetosGerais/RQ2/extraindoVersaoAtualDoFramework/Android.csv")
# spring_versions = open("/home/gabriel/Documentos/ic2/analiseDosProjetosGerais/RQ2/delay/logs/spring-versions.txt")
#

# for version in spring_versions:
#     version = version.replace("\n", "")
#     version = version.split(";")
#     versoes_do_spring[version[1]] = datetime.datetime.strptime(version[0], "%Y-%m-%d %H:%M:%S %z")
#
# # para cada arquivo de config
# for arquivo in arquivos_de_configuracao:
#     primeiro = True
#     versao_corrente = ''
#     #   para cada commit
#     arquivo_de_commits = open(
#         "/home/gabriel/Documentos/ic2/analiseDosProjetosGerais/RQ2/delay/logs/" + arquivo["projeto"] + ".txt")
#     commits = list()
#     for linhas_commits in arquivo_de_commits:
#         linhas_commits = linhas_commits.replace("\n", "")
#         linhas_commits = linhas_commits.split(";")
#         # 2010-06-18 12:33:58 +0000
#         commit = {
#             "hash": linhas_commits[0],
#             "data": datetime.datetime.strptime(linhas_commits[1], "%Y-%m-%d %H:%M:%S %z")
#         }
#         commits.append(commit)
#     # dou checkout no commit
#     for commit in commits:
#         try:
#             repo = Repo(
#                 "/home/gabriel/Documentos/ic2/analiseDosProjetosGerais/repositorios/" + arquivo["dono"] + "/" + arquivo[
#                     "projeto"])
#             repo.git.checkout(commit["hash"])
#             arquivo_de_configuracao = open(arquivo["caminho"]).read()
#         except:
#             continue
#
#         if ("Spring" == arquivo["framework"]):
#             posicao = arquivo_de_configuracao.find("org.springframework.boot")
#             versao = arquivo_de_configuracao[posicao:]
#             posicao = versao.find("version")
#             versao = versao[posicao:]
#             posicao = versao.find(">")
#             versao = versao[posicao + 1:]
#             posicao = versao.find("<")
#             versao = versao[:posicao]
#             versao = versao.replace("'", "")
#             if ("RELEASE" in versao and versao != versao_corrente and "2.2.0" not in versao):
#                 # calcular o delay
#                 delay = commit["data"] - versoes_do_spring[versao]
#                 if (primeiro == True):
#                     primeiro = False
#                     versao_corrente = versao
#                     continue
#                 print(arquivo["framework"] + "," + arquivo["dono"] + "/" + arquivo["projeto"] + "," + arquivo[
#                     "caminho"] + "," + versao + "," + str(delay.days) + "," + "Data do commit: " + commit[
#                           "data"].strftime("%Y-%m-%d %H:%M:%S") + "," + "Data de lancamento da versao " +
#                       versoes_do_android[versao].strftime("%Y-%m-%d %H:%M:%S"))
#                 # atualizar o versao_corrente
#                 versao_corrente = versao
#         elif ("Android" == arquivo["framework"]):
#             posicao_inicial = arquivo_de_configuracao.find("compileSdkVersion")
#             compileSdkVersion = arquivo_de_configuracao[posicao_inicial:]
#             posicao_inicial = compileSdkVersion.find(" ")
#             compileSdkVersion = compileSdkVersion[posicao_inicial + 1:]
#             posicao_final = compileSdkVersion.find("\n")
#             compileSdkVersion = compileSdkVersion[:posicao_final]
#             versao = compileSdkVersion
#             if (versao != '' and len(versao) < 3 and int(versao) > 19 and versao != versao_corrente):
#                 delay = commit["data"] - versoes_do_android[versao]
#                 if (primeiro == True):
#                     primeiro = False
#                     versao_corrente = versao
#                     continue
#                 print(arquivo["framework"] + "," + arquivo["dono"] + "/" + arquivo["projeto"] + "," + arquivo[
#                     "caminho"] + "," + versao + "," + str(delay.days) + "," + "Data do commit: " + commit[
#                           "data"].strftime("%Y-%m-%d %H:%M:%S") + "," + "Data de lancamento da versao " +
#                       versoes_do_android[versao].strftime("%Y-%m-%d %H:%M:%S"))
#                 versao_corrente = versao
