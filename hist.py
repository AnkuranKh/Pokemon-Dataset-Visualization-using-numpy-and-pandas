import numpy as py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

df=pd.read_csv('pokemon.csv')
print(df)

#histogram
base_color=sb.color_palette()[2]
plt.hist(data=df,x='speed',color=base_color,bins=5)

plt.show()