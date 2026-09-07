import pandas as pd
import numpy as np

d = {'First Score': [100, 90, np.nan, 95], 'Second Score': [30, 45, 56, np.nan],'Third Score': [np.nan, 40, 80, 98]}
df = pd.DataFrame(d)

print(df)
print(df['First Score'].describe())

mv = df.isnull()
mv = df.fillna(0)
print(mv.isnull())
print(mv)
print(mv['First Score'].describe())


import pandas as pd

# Create a hard-coded sample DataFrame with duplicates
data = {
    'Name': ['Arun', 'Baby', 'Arun', 'Dhruv', 'Lakshmi','Arun'],
    'Age': [25, 30, 25, 45, 30,35],
    'Department': ['HR', 'IT', 'HR', 'Finance', 'HR','HR']
}

df = pd.DataFrame(data)
print(df)

# 1. Default: Drop rows that are identical across ALL columns
df_no_dupes = df.drop_duplicates()
print(df_no_dupes)

# 2. Subset: Drop duplicates based only on a specific column (e.g., 'Name')
df_unique_names = df.drop_duplicates(subset=['Name'])
print(df_unique_names)

# 3. Custom: Keep the LAST occurrence of a duplicate instead of the first
df_last_dup = df.drop_duplicates(subset=['Name'], keep='last')
print(df_last_dup)
