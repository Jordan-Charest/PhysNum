


def trapeze(f, N, a, b, *args):
    h = (b-a)/N

    s = 0.5*f(a, *args)+0.5*f(b, *args)
    for i in range(1,N):
        s += f(a+i*h, *args)
    
    return h*s

### test

#def func(x):
#    return x**4 - 2*x + 1

#rep = trapeze(func, 100, 0, 2)
#print(rep)