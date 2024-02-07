import math

def xn1(xn_1, f_xn_1, xn, f_xn):
    return (xn -((f_xn * (xn - xn_1))/(f_xn - f_xn_1)))
    
def f(x):
    return (math.sin(math.radians(x)) + math.cos(math.radians(x)) - 1)

def eps(xn1, xn):
    return ((xn1- xn)/xn1)

Xn_1 = float(input("Enter Xn-1: "))
Xn = float(input("Enter Xn: "))
f_Xn_1 = f(Xn_1)
f_Xn = f(Xn)
Xn1 = xn1(Xn_1, f_Xn_1, Xn, f_Xn)
f_Xn1 = f(Xn1)
p = eps(Xn1, Xn)
print('\n Xn-1: %0.4f  f(Xn-1): %0.4f  Xn: %0.4f  f(Xn): %0.4f  Xn+1: %0.4f  f(Xn+1): %0.4f  EPS: %0.4f' % (Xn_1, f_Xn_1, Xn, f_Xn, Xn1, f_Xn1, p ))