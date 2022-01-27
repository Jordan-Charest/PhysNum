


def trapeze(f, N, a, b):
    h = (b-a)/N

    s = 0.5*f(a)+0.5*f(b)
    for i in range(1,N):
        s += f(a+i*h)
    
    return h*s

### test

def func(x):
    return x**4 - 2*x + 1

rep = trapeze(func, 10, 0, 2)
print(rep)