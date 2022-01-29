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

ne = densite_os

rho = 1850

# On intègre par la méthode des trapèzes et la méthode de Romberg avec une
# énergie d'entrée de 150 MeV

Ti = 2.4033*10**(-11) # en J

# test des trapezes avec 100 tranches

def func(T):
    return pouvoir_arret(T)**(-1)

rep_trapezes = trapeze(func, 100, 0, Ti) * rho

print("reponse avec trapezes, os=",rep_trapezes)
