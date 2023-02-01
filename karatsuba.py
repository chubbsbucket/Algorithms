# multiplies two integers using karatsuba technique
import math

def karatsuba(x, y):

    if x < 10 and y < 10:
        return x * y

    nx = int(math.log(x, 10)) + 1
    ny = int(math.log(y, 10)) + 1

    a = x // (10 ** (nx // 2))
    b = x % (10 ** (nx // 2))

    c = y // (10 ** (ny // 2))
    d = y % (10 ** (ny // 2))

    ac = karatsuba(a, c)
    bd = karatsuba(b ,d)
    bc = karatsuba(b, c)
    ad = karatsuba(a, d)

    xy = (10 ** (nx // 2 + ny // 2)) * ac + (10 ** (ny // 2)) * bc + (10 ** (nx // 2)) * ad + bd

    return xy


Number1 = int(input("First Integer:"))
Number2 = int(input("Second Integer:"))

x = karatsuba(Number1, Number2)

print ("Answer:" + str(x))