# source https://github.com/sahilgarg2814/avisoft/blob/main/feburary/day11_12_feb.ipynb
import numpy as np
import matplotlib.pyplot as plt
x = [0,1,2,3,4]
y = [0,2,4,6,8]

x=np.array(x)
y=np.array(y)

print(x)
type(x)
plt.plot(x,y,label='2x',color='blue',linewidth=1,marker='^',linestyle='--',markersize=5,markeredgecolor='blue')
#plt.plot(x,y,'b^--',label='2x)
# fmt=[color][marker][line]

x2=np.arange(0,5,0.5)

plt.plot(x2[:6],x2[:6]**2,'r',label='x^2')
plt.plot(x2[5:],x2[5:]**2,'r--')

plt.title("Our first graph",fontdict={'fontname':'Comic Sans Ms','fontsize':20})

plt.xlabel("X axis")
plt.ylabel("Y axis")

plt.legend()

plt.show()