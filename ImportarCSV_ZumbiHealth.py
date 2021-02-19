import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/santanche/lab2learn/master/data/zombie/zombie-health/zombie-health-symptoms-diagnostic.csv')

df.to_csv('zombie-health-symptoms-diagnostic.csv')