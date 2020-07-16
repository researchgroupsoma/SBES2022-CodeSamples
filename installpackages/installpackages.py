import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def installpackages():
    print("Installing PyGithub")
    install("PyGithub")
    print("Installing GitPython")
    install("GitPython")
    print("Installing stackapi")
    install("stackapi")
    print("Installing JPype1")
    install("JPype1")
    print("Installing Pandas")
    install("pandas")
