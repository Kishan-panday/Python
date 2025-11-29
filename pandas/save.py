import pandas as pd

data = {
    "Name":['Ram','Shyam','Mohan'],
    "Age":[10,25,34],
    "City":['Delhi','Mumbai','Kanpur']
}
df = pd.DataFrame(data)
print(df)
df.to_csv("output.csv",index=False)
df.to_csv("output.xlsx",index=False)