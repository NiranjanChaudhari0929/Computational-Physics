from numpy import random 
import numpy as np


def funct(x):
  return  (1/(1+x**2))  #return keyword is necessary

a=float(input("Enter lower limit : "))
b=float(input("Enter upper limit : "))
N=int(input("Number of parts to be taken   : "))
h=float((b-a)/N)
s=0

r=np.random.rand(N)

for i in range(0,N):
 s+=h*funct(r[i])

print("Integral calculated using Monte Carlo method is :",s)
