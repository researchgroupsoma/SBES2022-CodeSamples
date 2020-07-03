import pandas as pd
import matplotlib.pyplot as plt

df_metrics = pd.read_csv("/home/gabriel/Documentos/gabrielsmenezes/pesquisamestrado/metricsbycommits/googlesamples/android-vision__output.csv", parse_dates=True, usecols=[3,4,5,6,7])
df_stackoverflow = pd.read_csv("/home/gabriel/Documentos/gabrielsmenezes/pesquisamestrado/stackoverflow/googlesamples/android-vision.csv", parse_dates=True, usecols=[7])


df_metrics['date'] = pd.to_datetime(df_metrics['date'].astype(str).str[:-6])
df_stackoverflow['question_creation_date'] = pd.to_datetime(df_stackoverflow['question_creation_date'])

df_stackoverflow.sort_values(by="question_creation_date")

df_metrics = df_metrics.set_index(df_metrics['date'])
df_stackoverflow = df_stackoverflow.set_index(df_stackoverflow['question_creation_date'])


df_stackoverflow["count_questions"] = 1

print(df_metrics.head())
print(df_stackoverflow.head())

df_stackoverflow=df_stackoverflow.groupby([(df_stackoverflow.index.year)]).sum()
df_metrics=df_metrics.groupby([(df_metrics.index.year)]).mean()

merge = pd.concat([df_metrics,df_stackoverflow], axis=1)


print(merge)

merge_norm = (merge-merge.mean())/merge.std()

cols_plot = ["numberOfJavaFiles","countLineCode/numberOfJavaFiles","SumCyclomaticStrict/CountDeclMethod","readability", "count_questions"]
axes = merge_norm[cols_plot].plot(title="Metricas do android-vision")
plt.show()
