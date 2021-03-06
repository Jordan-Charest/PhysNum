from constantes import *
from pouvoir_arret import pouvoir_arret
import numpy as np
from methode_trapezes import trapeze
from methode_romberg import romberg
from densite_electrons import densiteelec, densite_os, densite_eau

# Pour calculer la portée, on doit intégrer l'inverse du pouvoir d'arrêt total
# par rapport à l'énergie selon la formule suivante:

# $$R_{CSDA}=\int_0^{T_i}\frac{\rho dT'}{S_{col}}$$

# On définit la densité d'électrons ne (par exemple ici pour les os)

ne = densite_os*10**6

rho = 1850

# On intègre par la méthode des trapèzes et la méthode de Romberg avec une
# énergie d'entrée de 150 MeV

Ti = 150 # en MeV

# test des trapezes avec 100 tranches

def fun(T, milieu):
    return pouvoir_arret(T, milieu)**(-1)

rep_trapezes = trapeze(fun, 100, 0, Ti, "eau") * dens["eau"][1] * 1000
print("reponse avec trapezes, eau=",rep_trapezes)

