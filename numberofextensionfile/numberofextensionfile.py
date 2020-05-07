import fnmatch
import os


def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        if '.git' in root:
            continue
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result


def remove_next_line(sample):
    return sample.replace('\n', '')


def output_write(framework, text):
    with open("numberofextensionfile/" + framework + "_numberofextensionfile_output.csv", "a") as f:
        f.write(text + "\n")
        f.close()


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
            find(extension, "/home/gabriel.menezes/Documentos/gabriel/pesquisamestrado/repositories/" + sample))


def numberofextensionfile(framework, projects):
    extensions = create_extension_files()
    output_write(framework,
                 'framework,project,java,properties,jar,build.gradle,pom.xml,manifest.xml,xml,bat,md,adoc,README,yaml,txt,sh,travis.yml,yml,cmd,kt,json,numberOfFiles,others')
    with open(projects) as samples:
        for sample in samples:
            sample = remove_next_line(sample)
            count_extension_files(extensions, sample)
            others = count_others(extensions)
            output = concat_output(extensions) + str(others)
            output_write(framework, framework+","+sample+","+output)
