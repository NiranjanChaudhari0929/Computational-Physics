def funct(x,y):
  return (x**2+y)



x0=float(input("The x coordinate given in the question as BVP :"))
y0=float(input("The y coordinate given in the question as BVP : "))

xn=float(input("The x coordinate at which value to be found : "))

n=int(input("The number of interations you want : "))

h=float((xn-x0)/n)

y1=0        #just initialising it 

while n!=0:
 f0=funct(x0,y0)
 f1=funct(x0+h/2,y0+h/2*f0)
 f2=funct(x0+h/2,y0+h/2*f1)
 f3=funct(x0+h,y0+h*f2)
 y1=y0+h/6*(f0+2*f1+2*f2+f3)
 y0=y1
 x0=x0+h
 n-=1
 
print("The value of the y to be found by Improved Euler method(Runge Kutta 2nd order method) is  ",y1)