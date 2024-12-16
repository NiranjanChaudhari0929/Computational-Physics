import numpy as np
import random

A=(1)/(1-np.exp(-np.pi))  #finding the value of constant A for this case

def P(x):            # defining the samping function
    p_x = (np.exp(-x)*A)
    return p_x

def F(x):       # defining the new function as limits changes from dx to dy
    f_x= 1/((A-x)*((np.log(1-x/A))**2 +(np.cos(np.log(1-x/A)))**2 ))
    return f_x


integral=0
n=100000
a=0
z=0

for i in range(n):               # running a for loop to get value of F(x)/P(x) at random points 
    a=random.uniform(0,1)
    z=(F(a))
    integral= integral + z
    

integral=integral/n  
print(integral)
    
