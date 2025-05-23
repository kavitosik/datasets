import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('titanic.csv')

df = df[df['Fare'] <= 300]

sns.boxplot(df['Fare'])
plt.title('Выбросы в Fare')
plt.show()
