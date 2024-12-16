import numpy as np
 
from numpy import random
import math

t=float(input("Thickness of plate: "))
pc=float(input("Probability of capturing: "))
ps=float(input("Probability of scattering: "))
n=int(input("Number of neutrons incident"))

a=np.random.rand(n)
cost=le=0
l=2 #(lambda value which is constant)
e=2.7
r=0 #reflected neutrons
t=0 #transmitted netrons
c=0#capturede electrons

for i in range(0,n):
    z=0
    
    
    if a[i]<ps:
     cost=1-2*a[i]
     le=l*math.log(a[i],e)
     z=z-le*cost
    
     if z<0:
        r=r+1
     else:
        t=t+1

    
    else:
        c=c+1
        
print("Number of reflected neutrons", r)
print("Number of transmitted neutrons",t)
print("Number of captured neutrons",c)


        
        
    
    
