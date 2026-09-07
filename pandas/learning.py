import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Name": ["A", "B", "C", "D"],
    "Marks": [90, np.nan, 80, 70]
})

#print(df.loc[df["Marks"] >= 80]["Marks"].mean())
#print(df[df["Marks"] >= 80]["Marks"].mean())


def f(i):
    print(i)

#f(4)


df = pd.DataFrame({
    "Name": ["A", "B", "C", "D"],
    "Marks": [90, 75, 82, 60]
})

avg = df["Marks"].mean()
#print(list(df[df["Marks"] < df["Marks"].mean()]["Name"]))


df = pd.DataFrame({
    "Name": ["Rahul", "Priya", "Neha", "Vikram", "Aditi"],
    "Marks": [85, 72, 91, 65, 88]
})

#print(df[df["Marks"] > df["Marks"].mean()].sort_values("Marks",ascending=False))

df = pd.DataFrame({
    "Name": ["Rahul", "Priya", "Neha", "Vikram", "Aditi"],
    "Marks": [85, 72, 91, 65, 88]
})

#print(df.sort_values("Marks",ascending=False))


df = pd.DataFrame({
    "Name": ["Rahul", "Priya", "Neha", "Vikram", "Aditi"],
    "Marks": [85, 72, 91, 65, 88]
})

#print(df.sort_values(by="Marks",ascending=False).head(3))
#print(df.nlargest(3, "Marks"))


df = pd.DataFrame({
    "Name": ["Rahul", "Priya", "Neha", "Vikram", "Aditi"],
    "Marks": [85, 72, 91, 65, 88]
})

#df["Result"] = np.where(df["Marks"] >= 75, "Pass", "Fail")
#print(df)

df = pd.DataFrame({
    "Name": ["Rahul", "Priya", "Neha", "Vikram", "Aditi"],
    "Marks": [85, 72, 91, 65, 88]
})
df["Grade"] = np.where(df["Marks"] >= 90, 'A', (np.where(df["Marks"] >= 80, 'B', 'C')))
#print(df)


df = pd.DataFrame({
    "Name": [
        "Rahul", "Priya", "Neha",
        "Vikram", "Aditi", "Karan",
        "Meera", "Arjun", "Sneha"
    ],
    "Department": [
        "CS", "CS", "CS",
        "ECE", "ECE", "ECE",
        "ME", "ME", "ME"
    ],
    "Marks": [
        85, 92, 74,
        65, 81, 78,
        88, 70, 91
    ]
})

df["Average"] = df.groupby("Department")["Marks"].transform("mean")
df["Status"] = np.where(df["Marks"] >= df["Average"], "Outstanding", "Normal")
df.drop(columns=["Average"], inplace=True)

df["Status"] = np.where(df["Marks"] >= df.groupby("Department")["Marks"].transform("mean"),"Outstanding","Normal")
#print(df)


df = pd.DataFrame({
    "City": ["Delhi", "Delhi", "Delhi",
             "Mumbai", "Mumbai", "Mumbai",
             "Chennai", "Chennai", "Chennai"],
    "Employee": ["A", "B", "C",
                 "D", "E", "F",
                 "G", "H", "I"],
    "Sales": [120, 150, 130,
              200, 180, 220,
              90, 100, 110]
})
df["CityAverage"] = df.groupby("City")["Sales"].transform("mean")
df["HighestSale"] = df.groupby("City")["Sales"].transform("max")
df["RemainingToBest"] = df.groupby("City")["Sales"].transform("max") - df["Sales"]


print(df)

