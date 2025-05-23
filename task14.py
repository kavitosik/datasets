import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('titanic.csv')

sns.boxplot(x='Pclass', y='Age', data=df)
plt.title('Age по классам')
plt.show()
