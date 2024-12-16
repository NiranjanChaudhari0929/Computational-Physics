import numpy as np
import matplotlib.pyplot as plt

p=0.01  #probability of decay
q=1-p
N=500   # number of particles

def decay(N):
    population=[]
    for t in range(100):
        r=np.random.random(N)      
        survive=np.sum(r<q)    #this step here provides us ability to manipulate the graph
        # print(survive)
        population.append((survive))
        N=survive
    return population
x=range(100)
plt.plot((x), decay(N)) 
plt.show()  