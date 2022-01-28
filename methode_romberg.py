# Méthode Romberg d'intégration numérique

from methode_trapezes import trapeze

def romberg(f, N_max, a, b, i_max):
    Rn = []
    N = int(N_max / 2**(i_max-1))
    for i in range(i_max):
        Rn.append([trapeze(f, N, a, b)])
        N = 2 * N
        for m in range(i):
            Rn[i].append(Rn[i][m] + (Rn[i][m] - Rn[i-1][m]) / (4**(m+2) - 1))
    
    return Rn[-1][-1]


# test

import numpy as np

def func(x):
    return np.exp(-x**2)

print(romberg(func, 4, 0, 1, 3))