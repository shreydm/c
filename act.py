import pandas as pd 
import csv
import plotly.graph_objects as pg

reader = pd.read_csv("data.csv")
si = reader.loc[reader['student_id']=='TRL_xsl']
#print(si.groupby("level")["attempt"].mean())

#graph = pg.Figure(pg.Bar(x=si.groupby("level")["attempt"].mean(),y=['level1','level2','level3','level4'],orientation="h"))
#graph.show()