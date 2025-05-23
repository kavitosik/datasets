import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("titanic.csv")

# df["Age"].hist(bins=20)
# plt.title("Распределение возрастов")
# plt.xlabel("Age")
# plt.ylabel("Count")
# plt.show()

sns.boxplot(x="Survived", y='Fare', data=df)
plt.title('Fare vs Survived')
plt.show()
