import numpy as np
from sqlalchemy import false, true
from densite_electrons import densiteelec
from energie_max_transfert import e_transf_max

# Variables du problème

# Pour calculer la densité électronique, on fournit une liste de données du
# NIST pour le matériau approprié et on effectue le calcul à l'aide du script
# "densite_electrons.py":

rho = 1 # Masse volumique du matériau
donnees = [] # Données du NIST pour le matériau

ne = densiteelec(rho, donnees)
c = 1       # vitesse de la lumière
re = 1      # rayon classique de l'électron
ne = 1      # densité électronique du matériau
me = 1      # masse au repos de l'électron
mp = 1      # masse au repos du proton
Z = 1       # charge de la particule
I = 1       # énergie moyenne d'excitation du matériau
beta = 1    # facteur de Lorentz
gamma = 1   # facteur de Lorentz
delta = 1   # terme considérant les effets de la polarisation
L1 = 1      # coefficient de correction de Barkas
L2 = 1      # coefficient de correction de Bloch
C = 1       # No fucking idea what that is
corr = true # true si e<3 MeV, false si e>3 MeV

def pouvoir_arret(re, me, c, ne, beta, gamma): # Pouvoir d'arrêt avec corrections
    te_max = e_transf_max(me, mp, c, gamma)

    const = 2 * np.pi * re**2 * me * c**2 * ne / beta**2
    parenth = np.log(2 * me * c**2 * gamma**2 * te_max / I**2) - (2 * beta**2)

    return (const * parenth)


def portee()
