# Boiler plate stuff to start the module
import jpype
from jpype import *
from utils import find_paths
from statistics import mean

class Readability(object):
	def __init__(self, project):
		super(Readability, self).__init__()
		self.project = project
		self.startJVM()
		self.readabilityPackage = JPackage("raykernel").apps.readability.eval.Main
		self.repositoryPath = "/home/gabriel/Documentos/gabrielsmenezes/pesquisamestrado/repositories/" + project


	def startJVM(self):
		if not jpype.isJVMStarted():
			jpype.startJVM(jpype.getDefaultJVMPath(), '-Djava.class.path=readability/readability.jar',  '-ea', '-Xmx2048M', convertStrings=True)


	def shutdownJVM(self):
		jpype.shutdownJVM()

	def getReadability(self):
		count = 0
		javaFiles = find_paths("*.java", self.repositoryPath)
		if len(javaFiles) == 0: return 0
		array = []
		for javaFile in javaFiles:
			array.append(float(self.readabilityPackage.getReadability(open(javaFile).read())))
		return mean(array)