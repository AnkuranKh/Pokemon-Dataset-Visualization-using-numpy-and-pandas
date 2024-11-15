import numpy as py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

pokemon=pd.read_csv('pokemon.csv')
print(pokemon.head(21))

print(pokemon.isna())
print(pokemon.isna().sum())

color_bar=sb.color_palette()[2]
gen_order=pokemon['generation_id'].value_counts().index
sb.countplot(data=pokemon,x='generation_id',color=color_bar, order=gen_order)

plt.show()

#color_bar2=sb.color_palette()[0]
#na_counts=pokemon.isna().sum()
#sb.barplot(na_counts.index.values,na_counts,color=color_bar2) To show the N/A values bar graph
#plt.xticks(rotation=90)


