import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def f(x):
    return x**2-3



xlist=np.linspace(-10,10,num=1000)
ylist=f(xlist)


x0=float(input("Enter the first limit of interval: "))   #f(x0) and f(x1) must have opposite values  #1
x1=float(input("Enter the second  limit of interval: "))  #3

N= int(input("Enter the iterations: "))

for i in range(0,N):
    x1=x0-f(x0)*(x1-x0)/(f(x1)-f(x0))
    
print(x1)
    
plt.plot(xlist,ylist)
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.legend("fn")
plt.title("Graph")
plt.show()