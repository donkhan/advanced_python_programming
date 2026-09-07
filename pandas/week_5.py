import pandas as pd

s = pd.Series([10, None, 30, None])
print(s.fillna(method='bfill').tolist())