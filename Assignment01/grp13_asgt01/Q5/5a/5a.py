#The Lorenz model is used to study the climate change and is given by dx/dt=a(y-x),dy/dt=-xz+bx-y,dz/dt=xy-cz
#where a = 10, c = 8/3 are some constants. b denotes the temperature difference between the top and bottom
#surfaces of the fluid. Solve the equations with RK-4 method with a = 10, c = 8/3 and b = 5, 10, 25. Plot the
#following:
#(a) z as a function of time for b = 5, 10, 25 for x = 1, y = z = 0. You can move from t = 0s to t = 50s. Is
#there any stricking difference at b = 25?
#(b) The trajectory of Lorenz model (for b = 25) in x − z plane with initial condition as x = 1, y = z = 0
#(c) The trajectory in yz plane when x = 0 with b = 25.
#(d) The trajectory in xz plane when y = 0 with b = 25.


from matplotlib import pyplot as plt

a=10;b=25;c=(8/3)  # initializing the constants as here b is 5,10,25 as per the case
x=0;y=0.000001;z=0 # given initial values
t=0.01             # step size
t_dash=0
X=[]
Y=[]
Z=[]
T=[]
for i in range(5000):
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


plt.plot(T,Z)
plt.xlabel("Time (s)")
plt.ylabel("Z axis")
plt.show()
