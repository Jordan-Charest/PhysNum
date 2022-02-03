import numpy as np
import matplotlib.pyplot as plt

# Fonction générale pour déterminer la densité électronique d'un matériau

# TODO: Ajouter une description !?!?!?
# TODO: vérifier limpact des erreurs d'arrondi
# Format de données: données = [[Z1, P1, M1], [Z2, P2, M2], ...]
# où Zn est le numéro atomique, Pn est la proportion massique et Mn est la masse volumique

def densiteelec(rho, donnees):
    nombreelec = []
    for i in donnees:
        nombreelec.append(i[1]*rho/i[2]*i[0]*6.02214076*10**(23))
    return sum(nombreelec)


# Eau liquide

densite_eau = densiteelec(1, [[1, 0.111894, 1.0079], [8, 0.888106, 15.999]])
rho_eau = 1

print("dens eau=",densite_eau)


# Os

donnees_os = [
    [1, 0.063984, 1.0079], 
    [6, 0.278000, 12.011], 
    [7, 0.027000, 14.007], 
    [8, 0.410016, 15.999], 
    [12, 0.002000, 24.305], 
    [15, 0.070000, 30.974], 
    [16, 0.002000, 32.06], 
    [20, 0.147000, 40.078]
    ]

densite_os = densiteelec(1.85, donnees_os)
rho_os = 1.850

print("densite os=",densite_os)