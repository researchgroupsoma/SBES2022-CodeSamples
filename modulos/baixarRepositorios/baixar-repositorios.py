import os

from git import Repo

frameworks = ['springsamples.txt', 'googlesamples.txt']
home = os.getenv('HOME')
caminho = home + '/Documentos/gabriel/pesquisa-mestrado/modulos/listaDeSamples/'
for framework in frameworks:
    print('framework: ' + framework)
    with open(caminho + framework) as samples:
        for sample in samples:
            sample = sample.replace('\n', '')
            print('sample: ' + sample)
            git_url = "https://github.com/" + sample + ".git"
            print('git_url: ' + git_url)
            repo_dir = home+"/Documentos/gabriel/pesquisa-mestrado/repositorios/"
            print("Baixando %s" % (sample))
            repo_dir = repo_dir + sample
            isdir = os.path.isdir(repo_dir)
            if isdir:
                print("Projeto " + sample + " já foi baixado")
                continue
            print('repo_dir+sample: ' + repo_dir)
            Repo.clone_from(git_url, repo_dir + sample)
            print("%s baixado com sucesso" % (sample))
            print(sample)
