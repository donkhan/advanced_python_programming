import pandas as pd


emp = pd.read_csv("employees.csv")

#print(emp)

# Detect Missing Values
#print(emp.isnull())
#print(emp.isna())


# count missing values
print(emp.isnull().sum())
e = emp.dropna()
#print(e)
#print(emp)
print("After dropping")
print(emp.isnull().sum())

# Filling Missing values
#print(emp.isnull().sum())
#emp["Age"] = emp["Age"].fillna(emp["Age"].median())
#print(emp.isnull().sum())


# Handle Outlier
#print(emp[emp["Age"] > 100])
#emp.loc[emp["Age"] > 100, "Age"] = emp["Age"].median()
#print(emp[emp["Name"] == "Eva"])

# Handle Duplicate
#print(emp[emp.duplicated()])
#emp = emp.drop_duplicates()
#print(emp[emp.duplicated()])

#EDA
# Frequency Count
#print(emp["Department"].value_counts())
# Max - cleaning data type

#print(emp["Salary"].dropna().max())
#print(emp.info())
# errors can be raise, coerce, ignore
#emp["Salary"] = pd.to_numeric(emp["Salary"], errors="coerce")
#print(emp["Salary"].dropna().max())


#Boolean Filtering
#print(emp[ emp["Age"] < 50])
