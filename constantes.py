from densite_electrons import densite_eau, densite_os, rho_eau, rho_os


###
# BUT: définir les constantes utilisées dans les autres scripts
###

c = 2.99792458 * 10**8                   # vitesse de la lumière [m/s]
re = 2.8179409238 * 10**(-15)         # rayon classique de l'électron [m]
me = 9.1093837015 * 10**(-31)     # masse au repos de l'électron [kg]
me_J = 8.186971882 * 10**(-14)
mp = 1.6726219236951 * 10**(-27)       # masse au repos du proton [kg]
mp_J = 1.50284161797 * 10**(-10)
Z = 1       # charge de la particule
I = 10       # énergie moyenne d'excitation du matériau
delta = 1   # terme considérant les effets de la polarisation
L1 = 1      # coefficient de correction de Barkas
L2 = 1      # coefficient de correction de Bloch
C = 1       # No fucking idea what that is
dens = {"eau": (densite_eau, rho_eau), "os": (densite_os, rho_os)}