# Méthode Romberg d'intégration numérique

from methode_trapezes import trapeze

def romberg(f, i_max, a, b, *args):
    Rn = []
    N = 1
    for i in range(i_max):
        Rn.append([trapeze(f, N, a, b, *args)])
        N = 2 * N
        for m in range(i):
            Rn[i].append(Rn[i][m] + (Rn[i][m] - Rn[i-1][m]) / (4**(m+1) - 1))
    return Rn[-1][-1]


# test

#import numpy as np

#def func(x):
#    return np.exp(-x**2)

#print(romberg(func, 3, 0, 1))