import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data)

print(df.describe())
print(df["calories"].describe())


data = pd.read_csv('../customers.csv')
print(data.describe())