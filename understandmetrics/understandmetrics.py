import subprocess
import os


def understandmetrics(framework, projects):
    understand_path = "/home/gabriel.menezes/Downloads/Understand-5.1.1024-Linux-64bit/scitools/bin/linux64/und"
    sample = "spring-guides/tut-rest"
    sample_repository = "repositories/" + sample
    output = "understandmetrics/" + sample + ".csv"

    bashCommand = "{0} create -db {1}.udb -languages java add {2} settings -metrics all settings -metricsOutputFile {3}.csv analyze metrics"\
        .format(understand_path, sample, sample_repository, output)
    print(subprocess.call(['bash', '-c', bashCommand]))
