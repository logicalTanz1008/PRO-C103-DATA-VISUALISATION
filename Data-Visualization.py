import plotly_express as px 
import pandas as pd 
df = pd.read_csv('c19.csv')
graph = px.scatter(df,x='date',y='cases',color='country')
graph.show()
