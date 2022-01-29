import numpy as np
from sqlalchemy import false, true
from densite_electrons import densiteelec, densite_os, densite_eau
from energie_max_transfert import e_transf_max
from constantes import *

# Variables du problème

# Pour calculer la densité électronique, on fournit une liste de données du
# NIST pour le matériau approprié et on effectue le calcul à l'aide du script
# "densite_electrons.py":

print("mp=",mp)
print("me=",me)

rho = 1850 # Masse volumique de l'os
I = 1.45798*10**(-17)# énergie moyenne d'excitation pour l'os
donnees = [] # Données du NIST pour le matériau

ne = densite_os*10**6
print("ne=",ne*10**(6))


def pouvoir_arret(T): # Pouvoir d'arrêt avec corrections
    gamma = T / (mp * c**2) + 1
    print("mp*c^2=",(mp*c**2))
    print("gamma=",gamma)
    beta = np.sqrt(1 - gamma**(-2))
    print("beta=",beta)

    te_max = e_transf_max(gamma)
    print("te_max=",te_max)

    const = 2 * np.pi * re**2 * me * c**2 * ne / beta**2
    parenth = np.log(2 * me * c**2 * gamma**2 * te_max / I**2) - (2 * beta**2)
    print("const=",const)
    print("parenth=",parenth)

    return (const * parenth)


print("test=",pouvoir_arret(2.4033*10**(-11)))
