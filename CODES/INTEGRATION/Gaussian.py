import numpy as np
import random as rand
import matplotlib.pyplot as plt

def funct(x):
 x=float(1/(1+x**2))
 return x



a=float(input("Enter lower limit: "))
b=float(input("Enter upper limit: ")) 
n=int(input("The number of points: "))

w=np.array([])                           #declring empty aray
y=np.array([])
f=np.array([])
p=np.array([])

for i in range(n):                          #taking user inout in array
    x=float(input("element for random numbers: "))
    w=np.append(w,x)
    
for i in range(n):                          #taking user inout in array
    x=float(input("element for y values: "))
    y=np.append(y,x)

for i in range(n):
    x=(b+a)/2+(b-a)*y/2
    f=np.append(f,funct((b+a)/2+(b-a)*y[i]/2))
    
p=np.multiply(w,f)

I=0
for i in range(0,n):
    I=I+p[i]

I=(b-a)*I/2   

print("The value of the integral is: ",I)
    
    



