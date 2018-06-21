import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


lesen = pd.read_csv('wetter2.csv')
print(lesen)
sns.lmplot(x='Monat', y='Temperatur', data=lesen)
plt.show()
