import subprocess
from utils import get_samples, output_write, remove_next_line, deal_with_empty_repo
from understandmetrics.UnderstandMetrics import UnderstandMetrics



def create_output_directory(metric, owner):
    subprocess.call(["bash", "-c", "mkdir -p "+metric+"/"+owner])


def extract_metrics_with_understand(udb_path, sample_path):
    understand_path = "/home/gabriel/Documentos/gabrielsmenezes/pesquisamestrado/understandmetrics/understand/scitools/bin/linux64/und"
    subprocess.call(["bash", "-c", "{0} create -languages java {1}".format(understand_path, udb_path) ])
    subprocess.call(["bash", "-c", "{0} add {1} {2}".format(understand_path, sample_path, udb_path)])
    subprocess.call(["bash", "-c", "{0} settings -metrics all {1}".format(understand_path, udb_path)])
    subprocess.call(["bash", "-c", "{0} settings -metricsOutputFile {1}.csv {1}".format(understand_path, udb_path)])
    subprocess.call(["bash", "-c", "{0}  -quiet analyze {1}".format(understand_path, udb_path)])
    subprocess.call(["bash", "-c", "{0} metrics {1}".format(understand_path, udb_path)])


def create_output(metrics):
    output = ""
    for metric, value in metrics:
        output += str(value) + ","
    return output[:-1]


def sum_metrics_per_sample(framework, sample, udb_path):
    with open(udb_path + ".csv") as file:
        metrics = [0] * 64
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
            metrics[-1] = number_of_java_file
        return metrics


def get_understand_metrics(framework, sample, udb_path, sample_path):
    extract_metrics_with_understand(udb_path, sample_path)
    metrics = sum_metrics_per_sample(framework, sample, udb_path)
    return UnderstandMetrics(metrics)

def understandmetrics(framework, projects):
    samples = get_samples(projects)
    owner = samples[0].split("/")[0]
    create_output_directory("understandmetrics", owner)
    output_write(framework, "understandmetrics", "understandmetrics","framework,projeto,AvgCyclomatic,AvgCyclomaticModified,AvgCyclomaticStrict,AvgEssential,AvgLine,AvgLineBlank,AvgLineCode,AvgLineComment,CountClassBase,CountClassCoupled,CountClassCoupledModified,CountClassDerived,CountDeclClass,CountDeclClassMethod,CountDeclClassVariable,CountDeclExecutableUnit,CountDeclFile,CountDeclFunction,CountDeclInstanceMethod,CountDeclInstanceVariable,CountDeclMethod,CountDeclMethodAll,CountDeclMethodDefault,CountDeclMethodPrivate,CountDeclMethodProtected,CountDeclMethodPublic,CountInput,CountLine,CountLineBlank,CountLineCode,CountLineCodeDecl,CountLineCodeExe,CountLineComment,CountOutput,CountPath,CountPathLog,CountSemicolon,CountStmt,CountStmtDecl,CountStmtExe,Cyclomatic,CyclomaticModified,CyclomaticStrict,Essential,Knots,MaxCyclomatic,MaxCyclomaticModified,MaxCyclomaticStrict,MaxEssential,MaxEssentialKnots,MaxInheritanceTree,MaxNesting,MinEssentialKnots,PercentLackOfCohesion,PercentLackOfCohesionModified,RatioCommentToCode,SumCyclomatic,SumCyclomaticModified,SumCyclomaticStrict,SumEssential,?,numberOfJavaFiles",True)

    for sample in samples:
        repositories_path = "/home/gabriel/Documentos/gabrielsmenezes/pesquisamestrado/repositories/"
        sample_path = repositories_path+sample
        udb_path = "understandmetrics/" + sample
        deal_with_empty_repo(sample)
        metrics = get_understand_metrics(framework, sample, udb_path, sample_path)
        output = create_output(metrics)
        output_write(framework, "understandmetrics", "understandmetrics", output, False)
