import pandas as pd

df = pd.read_csv("/tmp/flavors_of_cocoa.csv")

#print(df['Rating'].max())
#print(df.info())

print(df.groupby("Company Location").size())


df_cars = pd.DataFrame({
    "Car name": ["A2", "C3", "D2", "A3", "C6"],
    "Type": ["Sedan", "SUV", "Hatchback", "Sedan", "MUV"],
    "Brand": ["ASP", "TRE", "ASP", "TOY", "TOY"],
    "Price (in lakhs)": [15, 20, 14, 13, 18]
})

#print(df_cars.describe())
