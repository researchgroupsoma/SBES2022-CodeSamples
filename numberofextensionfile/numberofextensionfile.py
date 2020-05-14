from utils import output_write, find_paths, get_samples
from utils.utils import print_status_samples


def create_extension_files():
    return {
        "*.java": "",
        "*.properties": "",
        "*.jar": "",
        "*build.gradle": "",
        "*pom.xml": "",
        "*manifest.xml": "",
        "*.xml": "",
        "*.bat": "",
        "*.md": "",
        "*.adoc": "",
        "*README.*": "",
        "*.yaml": "",
        "*.txt": "",
        "*.sh": "",
        "*travis.yml": "",
        "*.yml": "",
        "*.cmd": "",
        "*.kt": "",
        "*.json": "",
        "*": ""
    }


def concat_output(extensions):
    output = ""
    for extension in extensions:
        output = output + str(extensions[extension]) + ","
    return output


def count_others(extensions):
    return extensions["*"] - extensions["*.java"] - extensions["*.properties"] - extensions["*.jar"] - extensions["*build.gradle"] - extensions["*.xml"] - extensions["*.bat"] - extensions["*.md"] - extensions["*.adoc"] - extensions["*.yaml"] - extensions["*.txt"] - extensions["*.sh"] - extensions["*.yml"] - extensions["*.cmd"] - extensions["*.kt"] - extensions["*.json"]


def count_extension_files(extensions, sample):
    for extension in extensions:
        extensions[extension] = len(
            find_paths(extension, "/home/gabriel.menezes/Documentos/gabriel/pesquisamestrado/repositories/" + sample))


def numberofextensionfile(framework, projects):
    print("Computing extension files")
    extensions = create_extension_files()
    measure = "numberofextensionfile"
    output_write(framework, measure, measure,
                 'framework,project,java,properties,jar,build.gradle,pom.xml,manifest.xml,xml,bat,md,adoc,README,yaml,txt,sh,travis.yml,yml,cmd,kt,json,numberOfFiles,others',
                 True)
    samples = get_samples(projects)
    for index, sample in enumerate(samples):
        print_status_samples(index+1, len(samples))
        count_extension_files(extensions, sample)
        others = count_others(extensions)
        output = concat_output(extensions) + str(others)
        output_write(framework, measure, measure, framework + "," + sample + "," + output, False)
