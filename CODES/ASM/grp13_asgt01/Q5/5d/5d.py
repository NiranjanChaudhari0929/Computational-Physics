import numpy as np
from matplotlib import pyplot as plt

a=10;b=25;c=(8/3)  # initializing the constants as here b is 5,10,25 as per the case
x=0;y=0.000001;z=0      # given initial values of X,Y,Z
t=0.01            # step size of t=0.01 is chosen for this case
t_dash=0
X=[]              # a list is created for X,Y,Z and T in which interations of X,Y,Z and T will be appended
Y=[]
Z=[]
T=[]
for i in range(5000):        # indexing the values of t with stepsize of 0.01
    t_dash= t_dash + t
    T.append(t_dash)

def K_x(p,q,r):              #  a function is defined for RK-4 (K) for X equation.
    k1=t*(a*(q-p))
    k2=t*(a*(q-(p+k1/2)))
    k3=t*(a*(q-(p+k2/2))) 
    k4=t*(a*(q-(p+k3)))
    k=(k1+2*k2 + 2*k3 + k4)/6
    return k

def K_y(p,q,r):             #  a function is defined for RK-4 (K) for Y equation.
    k1=t*(-p*r + b*p-q)
    k2=t*(-p*r+b*p-(q+k1/2))
    k3=t*(-p*r + b*p - (q+k2/2))
    k4=t*(-p*r+b*p-(q+k3))
    k=(k1+ 2*k2+ 2*k3 + k4)/6
    return k

def K_z(p,q,r):             #  a function is defined for RK-4 (K) for Z equation.
    k1=t*(p*q-c*r)
    k2=t*(p*q-c*(r+k1/2))
    k3=t*(p*q-c*(r+k2/2))
    k4=t*(p*q-c*(r+k3))
    k=(k1+2*k2+ 2*k3 + k4)/6
    return k   

for i in range (5000):     # for loop is created to index values of X,Y,Z simultaneously
    x=x + K_x(x,y,z)
    y= y + K_y(x,y,z)
    z= z + K_z(x,y,z)
    X.append(x)
    Y.append(y)
    Z.append(z)

plt.plot(X,Z)
plt.xlabel("X axis")
plt.ylabel("Z axis")
plt.title("y=0,b=25")
plt.show()
