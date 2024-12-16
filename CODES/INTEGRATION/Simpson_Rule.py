import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def funct(x):
  return  (1/(1+x**2))

a=float(input("Enter lower limit : "))
b=float(input("Enter upper limit : "))
N=float(input("Number of parts to be divided in  : "))
h=float((b-a)/N)
s=float(1/3*h*(funct(a)+funct(b)))
s1=0
s2=0

xlist=np.linspace(-10,10,num=1000)
ylist=funct(xlist)

k=a+h
while k<b:
 s1+=4*funct(k)
 k+=2*h
s1=s1*h/3

k=a
k=a+2*h
while k<b:
 s2+=2*funct(k)
 k+=2*h
s2=s2*h/3

s+=s1+s2
print("Integral calculated using Simpson 3 point rule  method is :",s)


plt.plot(xlist,ylist)
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.legend("fn")
plt.title("graph")
plt.show()