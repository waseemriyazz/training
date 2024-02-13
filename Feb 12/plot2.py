#source https://github.com/sahilgarg2814/avisoft/blob/main/feburary/day11_12_feb.ipynb

import pandas as pd
import matplotlib.pyplot as plt
file=pd.read_csv("Feb 12/gas_prices.csv")
plt.xticks(file['Year'][::3],rotation=90)
plt.plot(file['Year'],file['Australia'],color='red',linewidth=1,marker='o',markersize=2,label="Australia")
plt.plot(file['Year'],file['Canada'],color='green',linewidth=1,marker='o',markersize=2,label='Canada')
plt.plot(file['Year'],file['France'],color='orange',linewidth=1,marker='o',markersize=2,label='France')
plt.plot(file['Year'],file['Germany'],color='yellow',linewidth=1,marker='o',markersize=2,label='Germany')
plt.plot(file['Year'],file['Italy'],color='hotpink',linewidth=1,marker='o',markersize=2,label='Italy')
plt.plot(file['Year'],file['Japan'],color='black',linewidth=1,marker='o',markersize=2,label='Japan')

plt.plot(file['Year'],file['USA'],color='blue',linewidth=1,marker='o',markersize=2,label='USA')


plt.legend()
plt.show()