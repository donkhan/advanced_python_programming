import pandas as pd


data = pd.read_csv('../customers.csv')
print(data.describe())
print(data.info())