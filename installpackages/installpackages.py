from pip import main as pipmain

def install(package):
    pipmain(['install', "-q", package])

def installpackages():
    install("PyGithub")
    install("GitPython")
    install("stackapi")
