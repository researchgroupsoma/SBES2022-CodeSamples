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


######RQ1

######Number of Java Files

######Android
android_samples = pd.read_csv("/home/gabriel/Documentos/gabrielsmenezes/ic/frameworkCodeSamples/Samples/Metrics - Android-Tool Understand.csv")
android_general_projects = pd.read_csv("/home/gabriel/Documentos/gabrielsmenezes/ic2/analiseDosProjetosGerais/RQ1/extraindoMetricasComUnderstand/metricas-android.csv")
analyze("Android Number of Java Files", android_samples["numberofFilesJava"], android_general_projects["numberOfJavaFiles"])


######Spring
spring_samples = pd.read_csv("/home/gabriel/Documentos/gabrielsmenezes/ic/frameworkCodeSamples/Samples/Metrics - Spring-Tool Understand.csv")
spring_general_projects = pd.read_csv("/home/gabriel/Documentos/gabrielsmenezes/ic2/analiseDosProjetosGerais/RQ1/extraindoMetricasComUnderstand/metricas-spring.csv")
analyze("Spring Number of Java Files", spring_samples["numberofFilesJava"], spring_general_projects["numberOfJavaFiles"])


######Lines of code per file

######Android
android_samples = pd.read_csv("/home/gabriel/Documentos/gabrielsmenezes/ic/frameworkCodeSamples/Samples/Metrics - Android-Tool Understand.csv")
android_samples["codeLinePerFile"] = android_samples["CountLineCode"]/android_samples["numberofFilesJava"]

android_general_projects = pd.read_csv("/home/gabriel/Documentos/gabrielsmenezes/ic2/analiseDosProjetosGerais/RQ1/extraindoMetricasComUnderstand/metricas-android.csv")
android_general_projects["codeLinePerFile"] = android_general_projects["CountLineCode"]/android_general_projects["numberOfJavaFiles"]

analyze("Android Lines of code per file", android_samples["codeLinePerFile"], android_general_projects["codeLinePerFile"])


######Spring
spring_samples = pd.read_csv("/home/gabriel/Documentos/gabrielsmenezes/ic/frameworkCodeSamples/Samples/Metrics - Spring-Tool Understand.csv")
spring_samples["codeLinePerFile"] = spring_samples["CountLineCode"]/spring_samples["numberofFilesJava"]

spring_general_projects = pd.read_csv("/home/gabriel/Documentos/gabrielsmenezes/ic2/analiseDosProjetosGerais/RQ1/extraindoMetricasComUnderstand/metricas-spring.csv")
spring_general_projects["codeLinePerFile"] = spring_general_projects["CountLineCode"]/spring_general_projects["numberOfJavaFiles"]

analyze("Spring Lines of code per file", spring_samples["codeLinePerFile"], spring_general_projects["codeLinePerFile"])

######Lines of code per file

######Android
android_samples = pd.read_csv("/home/gabriel/Documentos/gabrielsmenezes/ic/frameworkCodeSamples/Samples/Metrics - Android-Tool Understand.csv")
android_samples["cyclomaticComplexity"] = android_samples["SumCyclomaticStrict"]/android_samples["CountDeclMethod"]

android_general_projects = pd.read_csv("/home/gabriel/Documentos/gabrielsmenezes/ic2/analiseDosProjetosGerais/RQ1/extraindoMetricasComUnderstand/metricas-android.csv")
android_general_projects["cyclomaticComplexity"] = android_general_projects["SumCyclomaticStrict"]/android_general_projects["CountDeclMethod"]

analyze("Android Cyclomatic Complexity per method", android_samples["cyclomaticComplexity"], android_general_projects["cyclomaticComplexity"])


######Spring
spring_samples = pd.read_csv("/home/gabriel/Documentos/gabrielsmenezes/ic/frameworkCodeSamples/Samples/Metrics - Spring-Tool Understand.csv")
spring_samples["cyclomaticComplexity"] = spring_samples["SumCyclomaticStrict"]/spring_samples["CountDeclMethod"]

spring_general_projects = pd.read_csv("/home/gabriel/Documentos/gabrielsmenezes/ic2/analiseDosProjetosGerais/RQ1/extraindoMetricasComUnderstand/metricas-spring.csv")
spring_general_projects["cyclomaticComplexity"] = spring_general_projects["SumCyclomaticStrict"]/spring_general_projects["CountDeclMethod"]

analyze("Spring Cyclomatic Complexity per method", spring_samples["cyclomaticComplexity"], spring_general_projects["cyclomaticComplexity"])



######Relative comment lines

######Android
android_samples = pd.read_csv("/home/gabriel/Documentos/gabrielsmenezes/ic/frameworkCodeSamples/Samples/Metrics - Android-Tool Understand.csv")
android_samples["RelativeLineCode"] = android_samples["CountLineComment"]/android_samples["numberofFilesJava"]

android_general_projects = pd.read_csv("/home/gabriel/Documentos/gabrielsmenezes/ic2/analiseDosProjetosGerais/RQ1/extraindoMetricasComUnderstand/metricas-android.csv")
android_general_projects["RelativeLineCode"] = android_general_projects["CountLineComment"]/android_general_projects["numberOfJavaFiles"]

analyze("Android Relative Commented Line of Code", android_samples["RelativeLineCode"], android_general_projects["RelativeLineCode"])


######Spring
spring_samples = pd.read_csv("/home/gabriel/Documentos/gabrielsmenezes/ic/frameworkCodeSamples/Samples/Metrics - Spring-Tool Understand.csv")
spring_samples["RelativeLineCode"] = spring_samples["CountLineComment"]/spring_samples["numberofFilesJava"]

spring_general_projects = pd.read_csv("/home/gabriel/Documentos/gabrielsmenezes/ic2/analiseDosProjetosGerais/RQ1/extraindoMetricasComUnderstand/metricas-spring.csv")
spring_general_projects["RelativeLineCode"] = spring_general_projects["CountLineComment"]/spring_general_projects["numberOfJavaFiles"]

analyze("Spring Relative Commented Line of Code", spring_samples["RelativeLineCode"], spring_general_projects["RelativeLineCode"])
