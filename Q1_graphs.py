import numpy as np
import matplotlib.pyplot as plt
from sqlalchemy import false, true
from densite_electrons import densiteelec, densite_os, densite_eau
from energie_max_transfert import e_transf_max
from constantes import *
from pouvoir_arret import pouvoir_arret


# Code pour tracer les graphiques de pouvoir d'arrêt, comme à la Question 1

T = np.linspace(3, 250, 10000)

S = []

for i in T:
    S.append(pouvoir_arret(i))


plt.plot(T, S)