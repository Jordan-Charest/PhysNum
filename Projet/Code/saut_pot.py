from functions import evolution_temporelle, psi_init, generate_animation
import numpy as np
import matplotlib.pyplot as plt


# Ce fichier permet de générer des animations pour un saut (marche) de potentiel.
# Un exemple du calcul des coefficients R et T se trouve aussi à la fin du fichier

# Constantes (SI)
hbar = 1.05457182 * 10**(-34)

# Paramètres
delta_x = 5*10**(-10)       # Largeur de la gaussienne (utiliser 1 et 5) [m]
x_0 = -0.5 * 10**(-8)       # Position de la gaussienne [m]
k_0 = 5 * 10 ** 10          # Nombre d'onde [rad/m]
N = 8000                    # Nombre de pas
dt = 1 * 10**(-17)          # Intervalle de temps [s]
t_max = N*dt                # Temps final [s]
m = 3 * 10**(-31)           # Masse de la particule [kg]
Nb = 50000                  # Nombres de divisions spatiales
V_0 = 10 * 10**(-19)        # Hauteur du potentiel [J]
vit = 10                    # Vitesse d'animation. 1 = normal, 10 = 10x plus vite

# Espace 1D
x = np.linspace(-10*10**(-8), 10*10**(-8), Nb)

# Potentiel 
V_liste = []
for i in x:
    if i > 0:
        V_liste.append(V_0)
    else:
        V_liste.append(0)
V = np.array(V_liste)

# Fonction d'onde initiale
psi_init = psi_init(x, x_0, delta_x, k_0)
psi_init = psi_init / np.sqrt(sum(np.abs(psi_init)**2)*20*10**(-8)/Nb)

# On éxécute la fonction d'évolution temporelle
t, psi = evolution_temporelle(psi_init, N, dt, V, m, Nb)

# On génère la figure
fig = plt.figure(figsize=(6, 5))
ax = fig.add_subplot(autoscale_on=True, xlim=(-100, 100), ylim=(0, 1*10**9))
ax.grid()

plt.axvline(x=0, color="black")

plt.ylabel("$|ψ|^2$")
plt.xlabel("$x$ [Å]")

line, = ax.plot([], [], "-", lw=1)
time_template = 'temps = %.3f fs'
pot_template = "V = %.3f eV"
time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)
pot_1 = ax.text(0.05, 0.75, '', transform=ax.transAxes)
pot_2 = ax.text(0.75, 0.75, '', transform=ax.transAxes)

# On subdivise l'array final de fonctions d'onde
psi_anim = psi[::20]

# On définit la fonction à animer qui sera appelée par FuncAnimation
def animate(i):

    this_psi = psi_anim[i]
    line.set_data(x*10**10, abs(this_psi)**2)
    time_text.set_text(time_template % (i*dt*20 * 10**15))
    pot_1.set_text(pot_template % (0))
    pot_2.set_text(pot_template % (6.484))
    return line, time_text

# On appelle la fonction generate_animation pour générer l'animation
file_path = "Projet\/animations\/saut_potentiel_50k.mp4"
generate_animation(fig, animate, len(psi_anim), file_path)

# détermination de R et T
R = []
T = []

psi_apres = psi[4000]
R = sum(np.abs(psi_apres[:2500]))
T = sum(np.abs(psi_apres[2500:]))

print(R/(R+T), T/(R+T))

# Résultats R, T:
# 1 : 0.4006630337341128 0.5993369662658873
# 2 : 0.9999999999933886 6.611443792618595e-12