from tkinter import X
import numpy as np
from numpy import pi, exp
import matplotlib.animation as animation

# constantes (SI)
hbar = 1.05457182 * 10**(-34)

# Définit la fonction d'onde initiale
# Arguments:
# x: linspace de l'espace d'intérêt en m
# x_0: position initiale du paquet d'onde
# delta_x: largeur de la gaussienne initiale
# k_0: nombre d'onde en rad/m
def psi_init(x, x_0, delta_x, k_0):
    psi_init = (1 / (2*np.pi*delta_x**2))**(1/4) * exp(1j*k_0*x - (x-x_0)**2 / (4*delta_x**2))
    return psi_init

# Effectue un pas de temps et retourne la nouvelle fonction d'onde
# Arguments:
# psi_1: Fonction d'onde initiale
# dt: pas de temps en secondes
# V: potentiel en Joules sous forme de linspace
# m: masse de la particule en kg
# Nb: nombre de divisions spatiales du linspace
def iteration_temporelle(psi_1, dt, V, m, Nb):
    phi = exp(-1j*V*dt / (2*hbar)) * psi_1
    phi_fourier = np.fft.fft(phi)
    k = np.fft.fftfreq(len(phi), 20*10**(-8)/Nb)
    T = hbar**2 * k**2 / (2 * m)
    fourier = exp(-1j*T*dt / (hbar)) * phi_fourier
    fourier_inv = np.fft.ifft(fourier)
    psi_2 = exp(-1j*V*dt / (2*hbar)) * fourier_inv
    return psi_2

# Fait évoluer la fonction du temps 0 au temps total N*dt et retourne une liste des fonctions d'ondes
# Arguments:
# psi_init: fonction d'onde au temps 0
# N: nombre de pas de temps
# dt: pas de temps
# V: potentiel en Joules sous forme de linspace
# m: masse de la particule en kg
# Nb: nombre de divisions spatiales du linspace
def evolution_temporelle(psi_init, N, dt, V, m, Nb):
    temps = np.linspace(0, N*dt, N)
    psi = [psi_init]
    for i in range(N):
        psi_2 = iteration_temporelle(psi[-1], dt, V, m, Nb)
        psi.append(psi_2)
    return temps, np.array(psi)

# Retourne l'énergie en eV
# Arguments:
# k_0: nombre d'onde de la particule en rad/m
# m: masse de la particule en kg
def energie(k_0, m):
    v = k_0 * hbar / m
    E_J = 0.5 * m * v**2
    return E_J*6.242*10**18


# Génère et sauvegarde l'animation de la fonction d'onde
# Arguments:
# fig: Figure pyplot prégénérée avec la légende, les axes, etc.
# func: fonction à animer
# length: longueur de l'animation (nombre de frames)
# path: chemin d'accès pour enregistrer le fichier .mp4 obtenu
def generate_animation(fig, func, length, path="Projet\/animations\/unnamed_animation.mp4"):
    ani = animation.FuncAnimation(fig, func, length, interval=1, repeat=False)
    writervideo = animation.FFMpegWriter(fps=60) 
    ani.save(path, writer=writervideo)