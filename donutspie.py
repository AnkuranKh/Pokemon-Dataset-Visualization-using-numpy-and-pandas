from turtle import color
import numpy as py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

df=pd.read_csv('pokemon.csv')
print(df.head())

orderedpie=df['generation_id'].value_counts()
plt.pie(orderedpie,labels=orderedpie.index, startangle=90,counterclock=False,wedgeprops={'width':0.4})# to make the donuts pie we need to add one more statement as wedgeprops
plt.axis('square');

plt.show()