from git import Repo
frameworks = ['googlesamples.txt', 'springsamples.txt']
for framework in frameworks:
	print('framework: ' + framework)
	with open (framework) as samples:
		for sample in samples:
			sample = sample.replace('\n','')
			print('sample: ' + sample)
			git_url = "https://github.com/" + sample + ".git"
			print('git_url: ' + git_url)
			repo_dir = "/home/gabriel.menezes/Documentos/mestrado/pesquisa/repositorios/"
			print("Baixando %s" % (sample))
			print('repo_dir+sample: ' + repo_dir+sample)
			Repo.clone_from(git_url, repo_dir+sample)
			print("%s baixado com sucesso" % (sample))
			print(sample)
