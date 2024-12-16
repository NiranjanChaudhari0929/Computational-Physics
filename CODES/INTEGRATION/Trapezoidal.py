import numpy as np
import matplotlib.pyplot as plt
import pandas as pd



def funct(x):
  return  (1/(1+x**2))

xlist=np.linspace(-10,10,num=1000)
ylist=funct(xlist)

a=float(input("Enter lower limit : "))
b=float(input("Enter upper limit : "))
N=float(input("Number of parts to be divided in  : "))
h=float((b-a)/N)
s=float(1/2*h*(funct(a)+funct(b)))

k=a+h
while k<b:
 s+=h*funct(k)
 k+=h

print("Integral calculated using Trapezodal method is :",s)

plt.plot(xlist,ylist)
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.legend("fn")
plt.title("Graph")
plt.show()
