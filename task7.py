import pandas as pd

df = pd.read_csv("Wine_dataset.csv")

class_vs_alcohol = df.crosstab(df['class'], df['Alcohol'])
print(class_vs_alcohol)
