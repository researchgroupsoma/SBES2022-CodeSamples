import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import copy

def gerarGraficos(sample):
	df_metrics = pd.read_csv("/home/gabriel/Documentos/gabrielsmenezes/pesquisamestrado/metricsbycommits/"+sample+"__output.csv", parse_dates=True, usecols=[3,4,5,6,7])
	df_stackoverflow = pd.read_csv("/home/gabriel/Documentos/gabrielsmenezes/pesquisamestrado/stackoverflow/"+sample+".csv", parse_dates=True, usecols=[7])


	df_metrics['date'] = pd.to_datetime(df_metrics['date'].astype(str).str[:-6])
	df_stackoverflow['question_creation_date'] = pd.to_datetime(df_stackoverflow['question_creation_date'])

	df_stackoverflow.sort_values(by="question_creation_date", inplace=True)

	df_metrics.set_index(df_metrics['date'], inplace=True)
	df_stackoverflow.set_index(df_stackoverflow['question_creation_date'], inplace=True)


	df_stackoverflow["count_questions"] = 1

	df_stackoverflow=df_stackoverflow.groupby([(df_stackoverflow.index.year), (df_stackoverflow.index.month)]).sum()
	df_metrics=df_metrics.groupby([(df_metrics.index.year), (df_metrics.index.month)]).last()

	merge = pd.concat([df_metrics,df_stackoverflow], axis=1)

	merge["count_questions"].fillna(0, inplace=True)

	merge.fillna(method="ffill", inplace=True)
	del merge['date']

	merge_norm = (merge-merge.mean())/merge.std()
	cols_plot = ["numberOfJavaFiles","countLineCode/numberOfJavaFiles","SumCyclomaticStrict/CountDeclMethod","readability", "count_questions"]
	axes = merge_norm[cols_plot].plot(title="Metricas do " + sample, figsize=(20,8))
	plt.savefig(sample+".png", bbox_inches = 'tight')
	plt.savefig(sample+".pdf", bbox_inches = 'tight')


samples = [
	"googlesamples/android-BluetoothLeGatt", 
	"googlesamples/android-Camera2Basic", 
	"googlesamples/android-play-location",
	"googlesamples/android-testing",
	"googlesamples/android-vision",
	"googlesamples/google-services",
	"spring-guides/tut-spring-boot-oauth2",
	"spring-guides/gs-spring-boot",
	"spring-guides/gs-rest-service",
	"Azure-Samples/active-directory-android",
	"Azure-Samples/storage-blob-java-getting-started"
]

[gerarGraficos(sample) for sample in samples]
