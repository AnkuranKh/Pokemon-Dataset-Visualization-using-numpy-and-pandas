import py_compile
from tokenize import PlainToken
from turtle import pd


import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sb

df=pd.read_csv('pokemon.csv')
print(df)

bins2=np.arange(0,df['speed'].max()+1,5)# note: by using numpy use of bins is ifferent as compared to directly using bins in matplotlib it is opposite to each other
plt.hist(data=df,x='speed',bins=bins2)

plt.show()