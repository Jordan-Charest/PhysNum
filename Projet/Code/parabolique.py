from functions import evolution_temporelle, psi_init, generate_animation
import numpy as np
import matplotlib.pyplot as plt

# Ce fichier permet de générer des animations pour le potentiel parabolique.


# Constantes (SI)
hbar = 1.05457182 * 10**(-34)

# Paramètres
delta_x = 1 * 10 ** (-10)       # Largeur de la gaussienne [m]
x_0 = 0                         # Position de la gaussienne [m]
k_0 = 5 * 10 ** 10              # Nombre d'onde (utiliser 1 et 5) [rad/m]
N = 8000                        # Nombre de pas
dt = 1 * 10**(-17)              # Intervalle de temps [s]
t_max = N*dt                    # Temps final [s]
m = 3 * 10**(-31)               # Masse de la particule [kg]
Nb = 5000                       # Nombre de divisions spatiales
omega = 1 * 10 ** 15            # Valeur d'oméga pour le potentiel parabolique [rad/s]
vit = 10                        # Vitesse d'animation. 1 = normal, 10 = 10x plus vite

# Espace 1D
x = np.linspace(-10*10**(-8), 10*10**(-8), Nb)

# Potentiel
V = 1/2 * m * omega**2 * x**2

# Fonction d'onde initiale
psi_init = psi_init(x, x_0, delta_x, k_0)
psi_init = psi_init / np.sqrt(sum(np.abs(psi_init)**2)*20*10**(-8)/Nb)

# On éxécute la fonction d'évolution temporelle
t, psi = evolution_temporelle(psi_init, N, dt, V, m, Nb)

# On génère la figure
fig = plt.figure(figsize=(6, 5))
ax = fig.add_subplot(autoscale_on=True, xlim=(-50, 50), ylim=(0, 0.8*10**10))
ax.grid()

ax.plot(x, V, color="black")

plt.ylabel("$|ψ|^2$")
plt.xlabel("$x$ [Å]")

line, = ax.plot([], [], "-", lw=1)
line2, = ax.plot([], [], "-", lw=1, color="black")
time_template = 'temps = %.3f fs'
pot_template = "V = $mω^2x^2/2$"
time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)
pot_1 = ax.text(0.05, 0.75, '', transform=ax.transAxes)

# On subdivise l'array final de fonctions d'onde
psi_anim = psi[::20]

# On définit la fonction à animer qui sera appelée par FuncAnimation
def animate(i):

    this_psi = psi_anim[i]
    line.set_data(x*10**10, abs(this_psi)**2)
    line2.set_data(x*10**10, V)
    time_text.set_text(time_template % (i*dt*20 * 10**15))
    pot_1.set_text(pot_template)
    return line, time_text

# On appelle la fonction generate_animation pour générer l'animation
file_path = "Projet\/animations\/parabolique.mp4"
generate_animation(fig, animate, len(psi_anim), file_path)