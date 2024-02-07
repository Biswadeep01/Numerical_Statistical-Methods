import math
#c.log(c)=1.2
#x.e^x = 2
def f(c):
    #return (c*math.log10(c) - 1.2)
    return (c * math.exp(c) - 2)

def formula(a, b):
    return ((a*f(b) - b*f(a))/(f(b) - f(a)))

def regular_falsi(a,b,e):
    y1 = f(b)
    y0 = f(a)
    if y0 * y1 < 0:
        c = formula(a, b)
        while abs(f(c)) > e:
            c = formula(a, b)
            if f(c) == 0:
                print('\nRequired root is : %0.4f' % c)
                return
            elif f(a)*f(c) < 0:
                b = c
                regular_falsi(a, b, e)
            else:
                a = c
                regular_falsi(a, b, e)
    else:
        print('Given guess values do not bracket the root')
        return
    
    return c

a = float(input("Enter X0: "))
b = float(input("Enter X1: "))
e = 0.0001
print('\n\n*** REGULAR FALSI METHOD IMPLEMENTATION ***')
root = regular_falsi(a,b,e)
print('\nRequired root is : %0.4f' % root)