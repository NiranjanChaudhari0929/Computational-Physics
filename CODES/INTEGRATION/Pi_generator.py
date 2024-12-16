from numpy  import random
import numpy as np


n=int(input("The number of data points to be taken as input: "))
x=np.random.rand(n)   #random point generation using numpy 
y=np.random.rand(n)

pointsincircle=0


for i in range(n):
    distance=(x[i]**2+y[i]**2)
    
    if distance <1:
        pointsincircle=pointsincircle+1
    
pi=4*pointsincircle/n
print(pi)


