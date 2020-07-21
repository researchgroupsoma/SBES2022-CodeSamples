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


######RQ2

######Lifetime

######Android
android_samples = pd.read_csv("/home/gabriel/Documentos/gabrielsmenezes/ic/frameworkCodeSamples/Samples/Metrics - Android-Tool Understand.csv")
android_general_projects = pd.read_csv("/home/gabriel/Documentos/gabrielsmenezes/ic2/analiseDosProjetosGerais/RQ2/lifetime/android.csv")
analyze("Android Lifetime", android_samples["Lifetime"], android_general_projects["Lifetime"])


######Spring
spring_samples = pd.read_csv("/home/gabriel/Documentos/gabrielsmenezes/ic/frameworkCodeSamples/Samples/Metrics - Spring-Tool Understand.csv")
spring_general_projects = pd.read_csv("/home/gabriel/Documentos/gabrielsmenezes/ic2/analiseDosProjetosGerais/RQ2/lifetime/spring.csv")
analyze("Spring Lifetime", spring_samples["Lifetime"], spring_general_projects["Lifetime"])



######Lifetime por commit

######Android
android_samples = pd.read_csv("/home/gabriel/Documentos/gabrielsmenezes/ic/frameworkCodeSamples/Samples/Metrics - Android-Tool Understand.csv")
android_general_projects = pd.read_csv("/home/gabriel/Documentos/gabrielsmenezes/ic2/analiseDosProjetosGerais/RQ2/lifetime/android.csv")
android_general_projects = android_general_projects["Lifetime"]/android_general_projects["commits"]
analyze("Android Lifetime per commit", android_samples["LifetimePerCommit"], android_general_projects)


# ######Spring
spring_samples = pd.read_csv("/home/gabriel/Documentos/gabrielsmenezes/ic/frameworkCodeSamples/Samples/Metrics - Spring-Tool Understand.csv")
spring_general_projects = pd.read_csv("/home/gabriel/Documentos/gabrielsmenezes/ic2/analiseDosProjetosGerais/RQ2/lifetime/spring.csv")
spring_general_projects = spring_general_projects["Lifetime"]/spring_general_projects["commits"]
analyze("Spring Lifetime per commit", spring_samples["LifetimePerCommit"], spring_general_projects)



###### Imports

######Android
samples = pd.read_csv("/home/gabriel/Documentos/gabrielsmenezes/ic/frameworkCodeSamples/Graficos/boxplotNumeroDeImports/importsRelativosAoNumeroDeJava/android.csv")["apenas do framework distinto"]
general_projects = pd.read_csv("/home/gabriel/Documentos/gabrielsmenezes/ic2/analiseDosProjetosGerais/RQ4/numeroDeImports/android.csv")["imports"]
analyze("Android relative framework import", samples, general_projects)


######Spring
samples = pd.read_csv("/home/gabriel/Documentos/gabrielsmenezes/ic/frameworkCodeSamples/Graficos/boxplotNumeroDeImports/importsRelativosAoNumeroDeJava/spring.csv")["apenas do framework distinto"]
general_projects = pd.read_csv("/home/gabriel/Documentos/gabrielsmenezes/ic2/analiseDosProjetosGerais/RQ4/numeroDeImports/spring.csv")["imports"]
analyze("Spring relative framework import", samples, general_projects)