#x3-2x-5
def f(n):
    return (n*n*n-2*n-5)

def bisection(x0,x1,e):
    step = 1
    print('\n\n*** BISECTION METHOD IMPLEMENTATION ***')
    condition = True
    while condition:
        x2 = (x0 + x1)/2
        print('Iteration-%d, x2 = %0.4f and f(x2) = %0.4f' % (step, x2, f(x2)))
        if f(x0) * f(x2) < 0:
            x1 = x2
        else:
            x0 = x2
        step = step + 1
        condition = abs(f(x2)) > e
    print('\nRequired root is : %0.8f' % x2)


x0 = 2
x1 = 3
e = 0.0001
bisection(x0,x1,e)