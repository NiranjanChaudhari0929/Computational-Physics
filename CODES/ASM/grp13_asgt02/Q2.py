#HALLEYS COMET


import numpy as np
from matplotlib import pyplot as plt

#initialising k with given value in question
k=39.5   

#iterating the sequence for n times
n=1000000

#defining empty lists to store iterative values 
X=[]
Y=[]
Vx=[]
Vy=[]
Ax=[]
Ay=[]
R=[]
T=[]

#initialising the distance coordinates of comet
x=1.97;y=0
# distance variable
r=(x*x+y*y)**0.5

#initialising the velocity coordinates of the comet
vx=0;vy=0.816
#defining the equations for acceleration followed by the intialsation 
ax=(-k*x)/(r*r*r)
ay=(-k*y)/(r*r*r)
ax_=0
ay_=0

#vmin=0.816
tau=1/n
t=0 # dummy variable
for i in range(n):
    t=t+i*tau
    T.append(t)                               #time stamp list 

for i in range(n):
    x=x+ tau*vx + ((tau*tau)*ax)/2
    X.append(x)                                #x coordinate list
    y=y + tau*vy + ((tau*tau)*ay)/2            
    Y.append(y)                                #y coordinate list
    r=(x*x+y*y)**0.5
    R.append(r)                                #distance from origin list
    ax_=ax
    ay_=ay   
    ax=(-k*x)/(r*r*r)
    Ax.append(ax)                              #acceleration along x axis 
    ay=(-k*y)/(r*r*r)
    Ay.append(ay)                              #acceleration along y axis
    
    vx=vx+ (tau*(ax+ax_))/2
    Vx.append(vx)                              #velocity in x direction
    vy=vy+ (tau*(ay+ay_))/2
    Vy.append(vy)                              #velocity in y direction

plt.plot(X,Y)                                  #Plotting characteristics 
plt.title("Orbit of Comet")             
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.axhline    
plt.show()
                                               
#END OF CODE 


    