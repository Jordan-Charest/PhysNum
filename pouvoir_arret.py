import numpy as np
from sqlalchemy import false, true
from densite_electrons import densiteelec
from energie_max_transfert import e_transf_max
from constantes import *

# Variables du problème

# Pour calculer la densité électronique, on fournit une liste de données du
# NIST pour le matériau approprié et on effectue le calcul à l'aide du script
# "densite_electrons.py":

rho = 1 # Masse volumique du matériau
donnees = [] # Données du NIST pour le matériau

ne = densiteelec(rho, donnees)

def pouvoir_arret(T): # Pouvoir d'arrêt avec corrections
    gamma = T / (mp * c**2) + 1
    beta = np.sqrt(1 - gamma**(-2))

    te_max = e_transf_max(me, mp, c, gamma)

    const = 2 * np.pi * re**2 * me * c**2 * ne / beta**2
    parenth = np.log(2 * me * c**2 * gamma**2 * te_max / I**2) - (2 * beta**2)

    return (const * parenth)
