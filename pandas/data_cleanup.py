import pandas as pd
import numpy as np

s = pd.Series([1, 2], dtype=np.int64).reindex([0, 1, 2])

#print(s.isna())

# define a dictionary with sample data which includes some missing values
data = {
    'A': [1, 2, 3, None, 5],
    'B': [None, 2, 3, 4, 5],
    'C': [1, 2, None, None, 5]
}

df = pd.DataFrame(data)
#print("Original Data:\n",df)
#print()

#print("Cleaned Data:\n",df.dropna())

# What is inplace
dx = df.fillna(0, inplace=False)
#print("after filling\n",dx)


# Fill with aggregate
data = {
    'A': [1, 2, 3, None, 5],
    'B': [None, 2, 3, 4, 5],
    'C': [1, 2, None, None, 5]
}
df = pd.DataFrame(data)
#print("Original Data:\n", df)
df.fillna(df.mean(), inplace=True)
#print("\nData after filling NaN with mean:\n", df)


# remove duplicates
data = {
    'A': [1, 2, 2, 3, 3, 4],
    'B': [5, 6, 6, 7, 8, 8]
}
df = pd.DataFrame(data)
print("Original DataFrame:\n", df.to_string(index=False))
# detect duplicates
print("\nDuplicate Rows:\n", df[df.duplicated()].to_string(index=False))
# remove duplicates based on column 'A' - check with 2 columns
df.drop_duplicates(subset=['A'], keep='first', inplace=True)
print("\nDataFrame after removing duplicates based on column 'A':\n", df.to_string(index=False))