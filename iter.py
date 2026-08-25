import pandas as pd
data={
    "name":["Shivam", "Suraj","Aditya"],
    "city":["Lucknow", "Gorakhpur", "Kanpur"],
    "course":["IT", "CSE", "AIML"],
}
df = pd.DataFrame(data)
print(df)
print(df.info())
print(df.describe())
df.to_csv("tech4b.csv")
studentdetails=pd.read_csv("tech4bclass.csv")
df=pd.DataFrame(studentdetails)
print(df)