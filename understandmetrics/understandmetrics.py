import subprocess
import os
from utils import get_samples, output_write, remove_next_line


def create_output_directory(owner):
    subprocess.call(["bash", "-c", "mkdir -p understandmetrics/"+owner])


def extract_metrics_with_understand(understand_path, udb_path, sample_path):
    subprocess.call(["bash", "-c", "{0} create -languages java {1}".format(understand_path, udb_path) ])
    subprocess.call(["bash", "-c", "{0} add {1} {2}".format(understand_path, sample_path, udb_path)])
    subprocess.call(["bash", "-c", "{0} settings -metrics all {1}".format(understand_path, udb_path)])
    subprocess.call(["bash", "-c", "{0} settings -metricsOutputFile {1}.csv {1}".format(understand_path, udb_path)])
    subprocess.call(["bash", "-c", "{0} analyze {1}".format(understand_path, udb_path)])
    subprocess.call(["bash", "-c", "{0} metrics {1}".format(understand_path, udb_path)])


def create_output(metrics, number_of_java_file):
    output = ""
    for metric in metrics:
        output += str(metric) + ","
    output += str(number_of_java_file)
    return output


def sum_metrics_per_sample(file, framework, metrics, sample):
    number_of_java_file = 0
    for line in file:
        line = remove_next_line(line)
        line = line.split(",")
        if line[0] == "File":
            number_of_java_file += 1
            for i in range(2, len(line)):
                line[i] = 0 if line[i] == '' else int(line[i])
                metrics[i] += line[i]
        metrics[0] = framework
        metrics[1] = sample
    return number_of_java_file


def understandmetrics(framework, projects):
    samples = get_samples(projects)
    owner = samples[0].split("/")[0]
    create_output_directory(owner)
    output_write(framework, "understandmetrics", "understandmetrics","framework,projeto,AvgCyclomatic,AvgCyclomaticModified,AvgCyclomaticStrict,AvgEssential,AvgLine,AvgLineBlank,AvgLineCode,AvgLineComment,CountClassBase,CountClassCoupled,CountClassCoupledModified,CountClassDerived,CountDeclClass,CountDeclClassMethod,CountDeclClassVariable,CountDeclExecutableUnit,CountDeclFile,CountDeclFunction,CountDeclInstanceMethod,CountDeclInstanceVariable,CountDeclMethod,CountDeclMethodAll,CountDeclMethodDefault,CountDeclMethodPrivate,CountDeclMethodProtected,CountDeclMethodPublic,CountInput,CountLine,CountLineBlank,CountLineCode,CountLineCodeDecl,CountLineCodeExe,CountLineComment,CountOutput,CountPath,CountPathLog,CountSemicolon,CountStmt,CountStmtDecl,CountStmtExe,Cyclomatic,CyclomaticModified,CyclomaticStrict,Essential,Knots,MaxCyclomatic,MaxCyclomaticModified,MaxCyclomaticStrict,MaxEssential,MaxEssentialKnots,MaxInheritanceTree,MaxNesting,MinEssentialKnots,PercentLackOfCohesion,PercentLackOfCohesionModified,RatioCommentToCode,SumCyclomatic,SumCyclomaticModified,SumCyclomaticStrict,SumEssential,?,numberOfJavaFiles",True)

    for sample in samples:
        understand_path = "/home/gabriel/Documentos/gabrielsmenezes/pesquisamestrado/understandmetrics/understand/scitools/bin/linux64/und"
        repositories_path = "/home/gabriel/Documentos/gabrielsmenezes/pesquisamestrado/repositories/"
        sample_path = repositories_path+sample
        udb_path = "understandmetrics/" + sample
        extract_metrics_with_understand(understand_path, udb_path, sample_path)

        with open(udb_path+".csv") as file:
            metrics = [0] * 63
            number_of_java_file = sum_metrics_per_sample(file, framework, metrics, sample)
            output = create_output(metrics, number_of_java_file)
            output_write(framework, "understandmetrics", "understandmetrics", output, False)



# repositorios = list()

# with open('/home/gabriel/Documentos/ic2/selecaoDosProjetosAleatoriamente/projetosAleatorios.csv') as arquivos_de_entrada:
#     for linha in arquivos_de_entrada:
#         linha = linha.replace('\n', '').split(',')
#         repositorio = {
#             "framework": linha[0],
#             "nome_do_dono": linha[1].split("/")[0],
#             "nome_do_projeto": linha[1].split("/")[1]
#         }
#         repositorios.append(repositorio)


# print('framework,projeto,AvgCyclomatic,AvgCyclomaticModified,AvgCyclomaticStrict,AvgEssential,AvgLine,AvgLineBlank,AvgLineCode,AvgLineComment,CountClassBase,CountClassCoupled,CountClassCoupledModified,CountClassDerived,CountDeclClass,CountDeclClassMethod,CountDeclClassVariable,CountDeclExecutableUnit,CountDeclFile,CountDeclFunction,CountDeclInstanceMethod,CountDeclInstanceVariable,CountDeclMethod,CountDeclMethodAll,CountDeclMethodDefault,CountDeclMethodPrivate,CountDeclMethodProtected,CountDeclMethodPublic,CountInput,CountLine,CountLineBlank,CountLineCode,CountLineCodeDecl,CountLineCodeExe,CountLineComment,CountOutput,CountPath,CountPathLog,CountSemicolon,CountStmt,CountStmtDecl,CountStmtExe,Cyclomatic,CyclomaticModified,CyclomaticStrict,Essential,Knots,MaxCyclomatic,MaxCyclomaticModified,MaxCyclomaticStrict,MaxEssential,MaxEssentialKnots,MaxInheritanceTree,MaxNesting,MinEssentialKnots,PercentLackOfCohesion,PercentLackOfCohesionModified,RatioCommentToCode,SumCyclomatic,SumCyclomaticModified,SumCyclomaticStrict,SumEssential,?,numberOfJavaFiles')
# for repositorio in repositorios:
#     metricas = [0] * 63
#     with open('/home/gabriel/Documentos/ic2/extraindoMetricasComUnderstand/metricas/'+repositorio['nome_do_projeto']+'.csv') as arquivo_de_metricas:
#         numero_de_java_file = 0
#         for linha in arquivo_de_metricas:
#             linha = linha.replace('\n', '').split(',')
#             if("File" == linha[0]):
#                 numero_de_java_file += 1
#                 for i in range(2, len(linha)):
#                     linha[i] = 0 if linha[i] == '' else int(linha[i])
#                     metricas[i] += linha[i]
#                 metricas[0] = repositorio['framework']
#                 metricas[1] = repositorio['nome_do_dono']+'/'+repositorio['nome_do_projeto']
#         for metrica in metricas:
#             print(str(metrica) + ',', end='')
#         print(str(numero_de_java_file))