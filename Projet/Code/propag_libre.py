from functions import evolution_temporelle, psi_init, generate_animation
import numpy as np
import matplotlib.pyplot as plt

# Ce fichier permet de générer des animations pour la propagation libre d'un paquet d'onde.

# Constantes (SI)
hbar = 1.05457182 * 10**(-34)

# Paramètres
delta_x = 5*10**(-10)       # Largeur de la gaussienne (utiliser 1 et 5) [m]
x_0 = -0.5 * 10**(-8)       # Position de la gaussienne [m]
k_0 = 5 * 10 ** 10          # Nombre d'onde (utiliser 1 et 5) [rad/m]
N = 8000                    # Nombre de pas
dt = 1 * 10**(-17)          # Intervalle de temps [s]
t_max = N*dt                # Temps final [s]
m = 3 * 10**(-31)           # Masse de la particule [kg]
Nb = 5000                   # Nombre de divisions spatiales
V = 0                       # Hauteur du potentiel [J]
vit = 10                    # Vitesse d'animation. 1 = normal, 10 = 10x plus vite

# Espace 1D
x = np.linspace(-10*10**(-8), 10*10**(-8), Nb)

# Fonction d'onde initiale
psi_init = psi_init(x, x_0, delta_x, k_0)
psi_init = psi_init / np.sqrt(sum(np.abs(psi_init)**2)*20*10**(-8)/Nb)

# On éxécute la fonction d'évolution temporelle
t, psi = evolution_temporelle(psi_init, N, dt, V, m, Nb)

# On génère la figure
fig = plt.figure(figsize=(6, 5))
ax = fig.add_subplot(autoscale_on=True, xlim=(-100, 100), ylim=(0, 1*10**9))
ax.grid()

plt.ylabel("$|ψ|^2$")
plt.xlabel("$x$ [Å]")

line, = ax.plot([], [], "-", lw=1)
time_template = 'temps = %.3f fs'
time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)

# On subdivise l'array final de fonctions d'onde
psi_anim = psi[::20]

# On définit la fonction à animer qui sera appelée par FuncAnimation
def animate(i):

    this_psi = psi_anim[i]
    line.set_data(x*10**10, abs(this_psi)**2)
    time_text.set_text(time_template % (i*dt*20 * 10**15))
    return line, time_text

# On appelle la fonction generate_animation pour générer l'animation
file_path = "Projet\/animations\/propagation.mp4"
generate_animation(fig, animate, len(psi_anim), file_path)