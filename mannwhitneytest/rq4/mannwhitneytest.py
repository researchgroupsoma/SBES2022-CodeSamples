from __future__ import division
import pandas as pd
from scipy.stats import wilcoxon


def cliffsDelta(lst1, lst2, **dull):

    """Returns delta and true if there are more than 'dull' differences"""
    if not dull:
        dull = {'small': 0.147, 'medium': 0.33, 'large': 0.474} # effect sizes from (Hess and Kromrey, 2004)
    m, n = len(lst1), len(lst2)
    lst2 = sorted(lst2)
    j = more = less = 0
    for repeats, x in runs(sorted(lst1)):
        while j <= (n - 1) and lst2[j] < x:
            j += 1
        more += j*repeats
        while j <= (n - 1) and lst2[j] == x:
            j += 1
        less += (n - j)*repeats
    d = (more - less) / (m*n)
    size = lookup_size(d, dull)
    return d, size


def lookup_size(delta: float, dull: dict) -> str:
    """
    :type delta: float
    :type dull: dict, a dictionary of small, medium, large thresholds.
    """
    delta = abs(delta)
    if delta < dull['small']:
        return 'negligible'
    if dull['small'] <= delta < dull['medium']:
        return 'small'
    if dull['medium'] <= delta < dull['large']:
        return 'medium'
    if delta >= dull['large']:
        return 'large'


def runs(lst):
    """Iterator, chunks repeated values"""
    for j, two in enumerate(lst):
        if j == 0:
            one, i = two, 0
        if one != two:
            yield j - i, one
            i = j
        one = two
    yield j - i + 1, two


def analyze(title, x, y):
	rst = wilcoxon(x, y)
	if rst.pvalue <= 0.05:
		print(title)
		print("Diferenca significante")
		print("p-value %.16f" % rst.pvalue)
		print("effect size: ", end="")
		print(cliffsDelta(x, y))
	else:
		print(title)
		print("Diferenca não significante")
	print("########")


######RQ4

######Number of forks

######Android
android_samples = pd.read_csv("/home/gabriel/Documentos/gabrielsmenezes/ic/frameworkCodeSamples/BuscadorDeMetadadosDeRepositoriosNoGit/android.csv")
android_general_projects = pd.read_csv("/home/gabriel/Documentos/gabrielsmenezes/ic2/analiseDosProjetosGerais/RQ1/obtendoOsMetadadosDosRepositorios/android.csv")
analyze("Android Number of Forks", android_samples["forks"], android_general_projects["forks"])


######Spring
spring_samples = pd.read_csv("/home/gabriel/Documentos/gabrielsmenezes/ic/frameworkCodeSamples/BuscadorDeMetadadosDeRepositoriosNoGit/spring.csv")
spring_general_projects = pd.read_csv("/home/gabriel/Documentos/gabrielsmenezes/ic2/analiseDosProjetosGerais/RQ1/obtendoOsMetadadosDosRepositorios/spring.csv")
analyze("Spring Number of Forks", spring_samples["forks"], spring_general_projects["forks"])


######Relative ahead forks

######Android
android_samples = pd.read_csv("/home/gabriel/Documentos/gabrielsmenezes/ic/frameworkCodeSamples/Graficos/BoxplotDaRazaoForkComAlteracao-Fork/android.csv")
android_general_projects = pd.read_csv("/home/gabriel/Documentos/gabrielsmenezes/ic2/analiseDosProjetosGerais/RQ4/extraindoTotalDeForks_ForksAhead/android.csv")
analyze("Android relative ahead forks", android_samples["forksAhead"]/android_samples["forks"], android_general_projects["forks_ahead"]/android_general_projects["forks"])
print()
######Spring
spring_samples = pd.read_csv("/home/gabriel/Documentos/gabrielsmenezes/ic/frameworkCodeSamples/Graficos/BoxplotDaRazaoForkComAlteracao-Fork/spring.csv")
spring_general_projects = pd.read_csv("/home/gabriel/Documentos/gabrielsmenezes/ic2/analiseDosProjetosGerais/RQ4/extraindoTotalDeForks_ForksAhead/spring.csv")
analyze("Spring relative ahead forks", spring_samples["forksAhead"]/spring_samples["forks"], spring_general_projects["forks_ahead"]/spring_general_projects["forks"])