import pandas as pd
import numpy as np

# From a dictionary
df1 = pd.DataFrame({
    "Name": ["Alice", "Bob"],
    "Age": [25, 30]
})

# From a list of lists
df2 = pd.DataFrame([
    ["Alice", 25],
    ["Bob", 30],
    ["Charles", 30]
], columns=["Name", "Age"])

# From a NumPy array
arr = np.array([
    ["Alice", 25],
    ["Bob", 30]
])
df3 = pd.DataFrame(arr, columns=["Name", "Age"])

df = pd.DataFrame({
    "A":[1,2],
    "B":[3,4]
})

df = pd.DataFrame({
    "A": [10, 20, 30],
    "B": [1,2,3]
})

#print(df["A"] + 5)
#print(len(df))


df = pd.DataFrame({
    "Name": ["Tom", "Jerry", "Spike"],
    "Marks": [70, 85, 90]
})


df = pd.DataFrame({
    "A": [10, 20, 30],
    "B": [1, 2, 3]
})

print(df["A"])
print(type(df["A"]))