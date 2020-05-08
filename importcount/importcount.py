from utils import remove_next_line, output_write, find_paths


def create_output(framework, imports, java_files_path, relative, sample):
    return framework + "," + sample + "," + str(len(imports)) + "," + str(len(java_files_path)) + "," + str(relative)


def calculate_relative(imports, java_files_path):
    if len(java_files_path) == 0:
        relative = 0
    else:
        relative = len(imports) / len(java_files_path)
    return relative


def get_imports_android(java_files_path):
    imports = set()
    for file in java_files_path:
        with open(file) as java_file:
            for line in java_file:
                line = remove_next_line(line)
                line = line.split(" ")
                if line[0] == "import":
                    lib = line[1].replace(";", "")
                    if lib.split(".")[0] == "android":
                        imports.add(lib)
    return imports


def get_imports_spring(java_files_path):
    imports = set()
    for file in java_files_path:
        with open(file) as java_file:
            for line in java_file:
                line = remove_next_line(line)
                line = line.split(" ")
                if line[0] == "import":
                    lib = line[1].replace(";", "")
                    if lib.split(".")[0] == "org" and lib.split(".")[1] == "springframework" and lib.split(".")[2] == "boot":
                        imports.add(lib)
    return imports


def get_imports(framework, java_files_path):
    if framework == "android":
        return get_imports_android(java_files_path)
    elif framework == "spring":
        return get_imports_spring(java_files_path)


def importcount(framework, projects):
    measure = "importcount"
    output_write(framework, measure, "framework,path,imports,javaFiles,imports/java_files", True)
    with open(projects) as samples:
        for sample in samples:
            sample = remove_next_line(sample)
            java_files_path = find_paths("*.java", "repositories/" + sample)
            imports = get_imports(framework, java_files_path)
            relative = calculate_relative(imports, java_files_path)
            output_write(framework, measure, create_output(framework, imports, java_files_path, relative, sample), False)