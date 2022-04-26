from functions import evolution_temporelle, psi_init, generate_animation
import numpy as np
import matplotlib.pyplot as plt

# Ce fichier permet de générer des animations pour un puits de potentiel infini (plutôt, approximé comme tel par rapport à l'énergie de la particule)
# Le cas n'a pas été étudié dans le rapport car il est très semblable à celui de la marche de potentiel, mais le présent fichier est fonctionnel.

# Constantes (SI)
hbar = 1.05457182 * 10**(-34)

# Paramètres
delta_x = 1*10**(-10)       # Largeur de la gaussienne (utiliser 1 et 5) [m]
x_0 = -0.3 * 10**(-8)       # Position de la gaussienne [m]
k_0 = 5 * 10 ** 10          # Nombre d'onde [rad/m]
N = 8000                    # Nombre de pas
dt = 1 * 10**(-17)          # Intervalle de temps [s]
t_max = N*dt                # Temps final [s]
m = 3 * 10**(-31)           # Masse de la particule [kg]
V_0 = 100000                # Hauteur du potentiel [J]               
vit = 10                    # Vitesse d'animation. 1 = normal, 10 = 10x plus vite

# Espace 1D
x = np.linspace(-10*10**(-8), 10*10**(-8), 5000)

# Potentiel
V_liste = []
for i in x:
    if abs(i) > 0.5*10**(-8):
        V_liste.append(V_0)
    else:
        V_liste.append(0)
V = np.array(V_liste)

# Fonction d'onde initiale
psi_init = psi_init(x, x_0, delta_x, k_0)
psi_init = psi_init / np.sqrt((sum(np.abs(psi_init)**2)))

# On éxécute la fonction d'évolution temporelle
t, psi = evolution_temporelle(psi_init, N, dt, V, m)

# On génère la figure
fig = plt.figure(figsize=(6, 5))
ax = fig.add_subplot(autoscale_on=True, xlim=(-100, 100), ylim=(0, 0.5))
ax.grid()

plt.axvline(x=-50, color="black")
plt.axvline(x=50, color="black")

plt.ylabel("$|ψ|^2$")
plt.xlabel("$x$ [Å]")

line, = ax.plot([], [], "-", lw=1)
time_template = 'temps = %.3f fs'
pot_template = "V = %.3f eV"
time_text = ax.text(0.03, 0.9, '', transform=ax.transAxes)
pot_1 = ax.text(0.03, 0.75, '', transform=ax.transAxes)
pot_2 = ax.text(0.38, 0.75, '', transform=ax.transAxes)
pot_3 = ax.text(0.78, 0.75, '', transform=ax.transAxes)

# On subdivise l'array final de fonctions d'onde
psi_anim = psi[::20]

# On définit la fonction à animer qui sera appelée par FuncAnimation
def animate(i):

    this_psi = psi_anim[i]
    line.set_data(x*10**10, abs(this_psi))
    time_text.set_text(time_template % (i*dt*20 * 10**15))
    pot_1.set_text(pot_template % (V_0))
    pot_2.set_text(pot_template % (0))
    pot_3.set_text(pot_template % (V_0))
    return line, time_text

# On appelle la fonction generate_animation pour générer l'animation
file_path = "Projet\/animations\/puits_infini.mp4"
generate_animation(fig, animate, len(psi_anim), file_path)