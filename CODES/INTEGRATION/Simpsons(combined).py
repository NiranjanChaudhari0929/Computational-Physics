# simpson 1/3 rule
def funct(x):
    return (1 / (1 + x ** 2))


a = float(input("Enter lower limit : "))
b = float(input("Enter upper limit : "))
N = float(input("Number of parts to be divided in  : "))


def simpson_one_by_three(a, b, N):
    h = (b - a) / N
    s = float(1 / 3 * h * (funct(a) + funct(b)))
    s1 = 0
    s2 = 0
    k = a + h
    while k < b:
        s1 += 4 * funct(k)
        k += 2 * h

    k = a + 2 * h

    while k < b:
        s2 += 2 * funct(k)
        k += 2 * h

    s += h / 3 * (s1 + s2)
    print("Integral calculated using Simpson 3 point rule  method is :", s)


simpson_one_by_three(a, b, N)


# simpson 3/8 rule
def simpson_three_by_eight(a,b,N):
    h = (b-a)/N
    sum = float(funct(a) + funct(b))
    for i in range(1, int(N)):
        if (i % 3 == 0):
            sum+= 2 * funct(a + i * h)
        else:
            sum+= 3 * funct(a + i * h)

    print((3*h*sum)/8)

simpson_three_by_eight(a, b, N)