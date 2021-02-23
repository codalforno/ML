import matplotlib.pyplot as plt
import pandas as pd
from sklearn import datasets
from sklearn import svm

def coding(col, codeDict):
  colCoded = pd.Series(col, copy=True)
  for key, value in codeDict.items():
    colCoded.replace(key, value, inplace=True)
  return colCoded

df = pd.read_csv('zombie-health-symptoms-diagnostic.csv')

print(df.head())

print('\n', df.columns)

print('\n', df.shape)

tgt = df[['diagnostic']]
print('\n', tgt)