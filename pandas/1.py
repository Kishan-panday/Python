import pandas as pd

df = pd.read_csv("CollegePlacement.csv",encoding="latin1")
print(df)
print(df.info())
# print("First five")
# print(df.head())


# print("Last five")
# print(df.tail())
print("describe")
print(df.describe)
print("select single column")
print(df["CGPA"])
print("more CGPA")
print(df[df["CGPA"]>9])
                    