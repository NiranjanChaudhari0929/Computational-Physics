
#Calculate the magnetic field from a straight wire by Trapeziodal
#and Gaussain methods. (a) Compare your results for the same grid
#size. (b) Plot a graph for magnetic field, By(x) as a function of
#x = 0 − 1.0. Consider two wires of lengths, 1 and 100.

from matplotlib import pyplot as plt
import numpy as np
from array import *

z1L = -0.5
z1U = 0.5
z2L = -50
z2U = 50

N = 1000
c=pow(10,-7)
I= 1


#function for finding value of given function 
def gcheck(x,z):
    g = c*I*x/pow((z*z+x*x),3/2)
    return g


#converting function for gaussain method
def convert(zL,zU,y):
    x= (zL+zU)/2 + ((zU-zL)*y)/2
    return x


#Code for trapezoidal method
def trapmain(x,zL,zU,o=1):
    i=1
    first = gcheck(x,zL)/2
    last = gcheck(x,zU)/2
    sum = first+last
    h=(zU-zL)/N
    z = z1L + h

    while(i<N):
        sum+=gcheck(x,z)
        z+=h
        i+=1
    
    total = h*sum
    if(o==1):
        print("\n\nThe length of wire is = ",zU-zL)
        print("\nValue of Magnetic field(integral) via Trapezoidal method is = ",total)
    return total


#Code of gaussian method
def gaussmain(x,zL,zU):
    y = array('d',[-0.9739065285,-0.8650633667,-0.6794095683,-0.4333953941,-0.148874339,0.148874339,0.4333953941,0.6794095683,0.8650633667,0.9739065285])
    W = array('d',[0.0666713443086835722,0.1494513492,0.2190863625,0.2692667193,0.2955242247,0.2955242247,0.2692667193,0.2190863625,0.1494513492,0.0666713443086835722])
    X = array('d',[convert(zL,zU,y[0]),convert(zL,zU,y[1]),convert(zL,zU,y[2]),convert(zL,zU,y[3]),convert(zL,zU,y[4]),convert(zL,zU,y[5]),convert(zL,zU,y[6]),convert(zL,zU,y[7]),convert(zL,zU,y[8]),convert(zL,zU,y[9])])

    #We are applying gaussian method for N=10
    i=0
    sum=0
    while(i<10):
        sum+=W[i]*gcheck(x,X[i])
        i+=1
    total = (zU-zL)*sum/2
    print("\n\nThe length of wire is = ",zU-zL)
    print("\nValue of Magnetic field(integral) via gaussian method is = ",total)
    return total

#We have taken initial perpendicular distance as 1m
gaussmain(1,z1L,z1U)
trapmain(1,z1L,z1U)
gaussmain(1,z2L,z2U)
trapmain(50,z2L,z2U)


#For wire length 1m
x_plt = np.arange(0.01, 1.01,0.01)     #we have taken numpy array in order of numbers


b_plt=[]    #b_plt=np.array([]) also allowed

i=0
while(i<100):
    b_plt.append((trapmain(x_plt[i],z1L,z1U,0)))
    i+=1


plt.plot(x_plt,b_plt)
plt.xlabel("x in m")
plt.ylabel("B in T ")
plt.title("Magnetic field(B) vs perpendicular distance(x)(L=1m)")
plt.show()



#For wire length 100m
b_plt=[]

i=0
while(i<100):
    b_plt.append((trapmain(x_plt[i],z2L,z2U,0)))
    i+=1



plt.plot(x_plt,b_plt)
plt.xlabel("x in m")
plt.ylabel("B in T ")
plt.title("Magnetic field(B) vs perpendicular distance(x)(L=100)")
plt.show()