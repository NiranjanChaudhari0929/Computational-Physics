import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def fn(x):                                              #define function to return the given
 return x**3 - x-3

def dfn(x):                                             # define function to return the derivative 
 return 3*x**2 - 1

x0=float(input("Enter initial guess : "))               # input of inital guess provided by  user which is 0.
tolerance=float(input("Enter tolerance : "))            # input of tolerance provided by the user 
iterations=int(input("Number of iterations  : "))       # input of iterations of code provided by user

xlist=np.linspace(-10,10,num=1000)
ylist=fn(xlist)

for i in range(iterations):                             # for loop constructed to iterate the values of x
   xnew=x0-fn(x0)/dfn(x0)                               # formula of Newton Raphson method
   if abs(xnew-x0)<tolerance: break                     # condition to end the loop when the difference of the 
                                                        #consectuive x values is less than tolerance
   x0=xnew                                              #the old value of x is given to new value of x 
  
print("The root of the equation by Newton raphson method is: ",x0)  #user is provided the output

plt.plot(xlist,ylist)
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.legend("fn")
plt.show()

