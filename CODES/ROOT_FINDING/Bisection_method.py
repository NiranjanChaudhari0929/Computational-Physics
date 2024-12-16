import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def f(x):
    return x**2-3

xlist=np.linspace(-10,10,num=1000)
ylist=f(xlist)


a=float(input("Enter the first limit of interval: "))
b=float(input("Enter the second  limit of interval: "))

N= int(input("Enter the iterations: "))

for i in range(0,N):
    x=(a+b)/2
    f(x)
    
    if f(x)>0:
        b=x
    else :
        a=x
        
        
print("The root is: ",x)
    
plt.plot(xlist,ylist)
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.legend("fn")
plt.title("Graph")
plt.show()