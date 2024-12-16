

#RANDOM WALK IN 3D,DONT RESTRICT WALKER ON DISCRETE LATTICE SITES 



# In this question, it is impossible to directly get three random no. a, b, c such that 
# sqrt(a**2 + b**2 + c**2) is 1, so instead, we'll generate direction, and we can use 
# radial coordinates, because we only need 2 coordinates, theta and phi(r = 1), so we'll
# go ahead with that. Then we notice that there is no way to directly do vector addition on 
# spherical vectors, we convert them back to cartesian vectors

import random
import math
import matplotlib.pyplot as plt
import numpy as np

def theta():
    return random.uniform(0,math.pi) # in range [0,180] == [0,pi]   #randomised values shall be returned 
def phi():
    return random.uniform(0,math.pi * 2) # in range [0, 360] == [0, 2*pi]   #randomised values shall be returned

d = 0
def sprToCrt(r, tht, ph): # This function converts Sperical coordinates to Cartesian
    x = r * math.sin(ph) * math.cos(tht)
    y = r * math.sin(ph) * math.sin(tht)
    z = r * math.cos(ph)
    return float(x), float(y), float(z)

r = 1
x = y = z = 0
t = [0.]  #t=np.array([]) ?
a = [0.]
xl = [0.]
yl = [0.]
zl = [0.]
n = int(input("Enter steps: "))
for i in range(n):
    tht = theta()
    ph = phi()
    x1, y1, z1 = sprToCrt(r, tht, ph)
    # print(x1, y1, z1)
    x1 += x
    y1 += y
    z1 += z
    xl.append(x1)
    yl.append(y1)
    zl.append(z1)
    # print(x1, y1, z1)
    z = z1
    x = x1
    y = y1
    a.append(x**2 + y**2 + z**2)
    t.append(t)       #t=np.append(t,t) ?

fig = plt.figure()
ax = plt.axes(projection ='3d')
ax.plot(xl, yl, zl, 'green')
ax.plot(0,0,0,'red')
plt.show()
m, b = np.polyfit(t, a, 1)
# print(m,b)
m = float(m)
b = float(b)
plt.plot(t, a, 'o')
plt.plot(t, m * np.asarray(t) + b, 'red')
print("Slope: ",m)
print("Coefficient: ",b)
plt.show()

