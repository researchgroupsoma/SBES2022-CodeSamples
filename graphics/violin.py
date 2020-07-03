import pandas as pd
import numpy as np
import matplotlib.pyplot as plot
from matplotlib import ticker as mticker

class Violin(object):
	def __init__(self, files, metric):
		super(Violin, self).__init__()
		self.files = files
		self.metric = metric
		self.data = self.getData()
		print(self.data)
		self.logData = self.getLogData()

	def getData(self):
		dataframes = [pd.read_csv(path) for path in self.files]
		data = [np.array(df[self.metric], dtype=float) for df in dataframes]
		data = [d[~np.isnan(d)] for d in data] #removendo os NaNs
		return data

	def getLogData(self):
		return [np.log10(d) for d in self.data]

	def save(self, title, xlabel, ylabel, filename):
		figure, axis = plot.subplots(nrows=1, ncols=1, figsize=(10,5))
		figure.suptitle(title, fontsize=16)
		axis.violinplot(self.logData, showextrema=False)
		axis.set_xlabel(xlabel, fontsize=14)
		axis.set_xticks([i+1 for i in range(len(self.logData))])
		axis.set_xticklabels(("Android", "Spring Boot", "AWS", "Azure"), fontsize=12)
		axis.set_ylabel(ylabel, fontsize=14)
		axis.boxplot(self.logData, showfliers=False, labels=["", "", "", ""], whis=0)
		
		median = [np.median(d) for d in self.data]
		log_median = [np.median(d) for d in self.logData]
		[axis.text(x=i+0.9,y=log_median[i]*1.1,s=str(median[i]), fontsize=16) for i in range(len(median))]

		axis.yaxis.set_major_formatter(mticker.StrMethodFormatter("$10^{{{x:.0f}}}$"))

		plot.savefig(filename)