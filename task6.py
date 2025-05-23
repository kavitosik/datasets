import pandas as pd

df = pd.read_csv("Wine_dataset.csv")
print(df.describe())
# x = df[['class', 'Alcohol']].nunique()
# print(x)
