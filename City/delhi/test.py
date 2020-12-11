import pandas as pd

df = pd.read_csv("IN_Delhi_NSITDwarka.MYD04.csv", header=None)
df = df.iloc[:, :-1]
df.columns= ['YYYY', 'MM', 'DD', 'Latitude', 'Longitude', 'AOD1', 'AOD3', 'STD3']
df.to_csv('IN_Delhi_NSITDwarka.MYD04.csv', index=False)
