import pandas as pd 
import csv
import plotly.graph_objects as pg

reader = pd.read_csv("data.csv")
#si = reader.loc[reader['student_id']=='TRL_xsl']
si = reader.groupby(["student_id", "level"], as_index=False)["attempt"].mean()
print(si)

graph = pg.scatter(si, x = 'student_id', y = 'level', size = 'attempt', color = 'attempt')
graph.show()
