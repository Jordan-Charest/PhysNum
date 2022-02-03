from constantes import *
import numpy as np


# Erreur sur l'intégration par la méthode des trapèzes selon l'équation d'Euler-Maclaurin

def erreur_trapeze(f, N, a, b):
    return 1/12 * (N / (b - a))**2 * (f(a) - f(b))


# dérivée déterminée analytiquement

def dS_dT(T):
    gamma = T / (mp*c**2) + 1
    a = 2*me*c**2
    b = 1 + (me/mp)**2
    d = 2 * (me/mp)
    return 2*np.pi*re**2*me / mp * gamma / (gamma**2-1) * (4*gamma**2 - 2*np.log(2*me*c**2*a*(gamma-1) / (I**2*(b+d))) - (d*gamma*(gamma**2-1)) / (b + d*gamma))

print(erreur_trapeze(dS_dT, 256, 0, 150))