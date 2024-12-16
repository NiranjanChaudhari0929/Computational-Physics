
def funct(x,y):
  return (x+y)



x0=float(input("The x coordinate given in the question as BVP :"))
y0=float(input("The y coordinate given in the question as BVP : "))

xn=float(input("The x coordinate at which value to be found : "))

n=int(input("The number of interations you want : "))

h=float((xn-x0)/n)

y1=0            #just initialising it 
for i in range(n): #or whule n!=0
 y1=y0+h*funct(x0+h/2,y0+h/2*funct(x0,y0))
 y0=y1
 x0=x0+h
 n-=1

print("The value of the y to be found by Modified Euler (Predictor corrector method) is  ",y1)