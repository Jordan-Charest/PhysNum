import numpy as np
from constantes import *

###
# BUT: Calculer l'énergie maximale trasnférable à un électron par le proton
# T_e^max
###

def e_transf_max(gamma):
    te_max = 2 * me * c**2 * (gamma**2 - 1) / (1 + 2*gamma*me/mp + (me/mp)**2)
    return te_max
