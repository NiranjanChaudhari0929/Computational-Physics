
def funct(x):
  return  (1/(1+x**2))

a=float(input("Enter lower limit : "))
b=float(input("Enter lower limit : "))
N=float(input("Number of parts to be divided in  : ")) #N is 4 here 
h=float((b-a)/N)
s=float(2*h/45*(7*funct(a)+32*funct(a+h)+12*funct(a+2*h)+32*funct(b-h)+7*funct(b)))

print("Integral calculated using Boole SPL rule  method is :",s)