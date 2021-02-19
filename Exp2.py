import matplotlib.pyplot as plt
import pandas as pd
from sklearn import datasets
from sklearn import svm

df = pd.read_csv('zombie-health-symptoms-diagnostic.csv')

print(df.head())

print('\n', df.columns)

print('\n', df.shape)

tgt = df[['diagnostic']]
print('\n', tgt)