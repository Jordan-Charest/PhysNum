from functions import evolution_temporelle, psi_init, energie, generate_animation
import numpy as np
import matplotlib.pyplot as plt

# Ce fichier permet de générer des animations pour la particule alpha dans un noyau d'uranium 238
# Comme mentionné dans le rapport, la méthode pseudo-spectrale ne donne pas de bons résultats pour cette situation, mais le code est fonctionnel.


# constantes (SI)
hbar = 1.05457182 * 10**(-34)
h = 6.62607015 * 10**(-34)
c = 299792458

# Paramètres de la fonction d'onde
delta_x = 0.1*10**(-15)                     # Largeur de la gaussienne [m]
x_0 = -3 * 10**(-15)                        # Position de la gaussienne [m]
k_0 = 9.7835 * 10 ** 14                     # Nombre d'onde [rad/m]
N = 8000                                    # Nombre de pas
dt = 0.5 * 10**(-23)                        # Intervalle de temps [s]
t_max = N*dt                                # Temps final [s]
m = 6.644 * 10**(-27)                       # Masse de la particule [kg]
V_0 = -1804.232 * 10**6 / (6.242*10**18)    # Hauteur du potentiel sphérique à l'intérieur du noyau [J]
V_1 = 4.615 * 10**(-26)                     # Hauteur du otentiel coulombien multiplié par x [J]
r = 1.2*10**(-15) * 238**(1/3)              # Rayon approx d'un noyau d'Uranium 238 [m]
Nb = 5000                                   # Nombre de divisions spatiales
# Selon le potentiel coulombien, la particule devrait faire un effet tunnel à environ x = 57,6 fm

# Espace 1D
x = np.linspace(-200*10**(-15), 200*10**(-15), Nb)

# Potentiel
V_liste = []
for i in x:
    if abs(i) < r:
        V_liste.append(V_0)
    else:
        V_liste.append(V_1/abs(i))
V = np.array(V_liste)

# Fonction d'onde initiale
psi_init = psi_init(x, x_0, delta_x, k_0)
psi_init = psi_init / np.sqrt((sum(np.abs(psi_init)**2))*400*10**(-15)/Nb)

# On éxécute la fonction d'évolution temporelle
t, psi = evolution_temporelle(psi_init, N, dt, V, m, Nb)

# On génère la figure
fig = plt.figure(figsize=(6, 5))
ax = fig.add_subplot(autoscale_on=True, xlim=(-100, 100), ylim=(0, 4*10**7))
ax.grid()

plt.axvline(x=-r*10**(15), color="black")
plt.axvline(x=r*10**(15), color="black")

plt.ylabel("$|ψ|^2$")
plt.xlabel("$x$ [fm]")

line, = ax.plot([], [], "-", lw=1)
time_template = 'temps = %.3f as'
pot_template = "V = %.3f MeV"
E_template = "E = %.3f MeV"
time_text = ax.text(0.03, 0.9, '', transform=ax.transAxes)
E_text = ax.text(0.03, 0.85, '', transform=ax.transAxes)
pot_1 = ax.text(0.03, 0.75, '', transform=ax.transAxes)
pot_2 = ax.text(0.38, 0.75, '', transform=ax.transAxes)
pot_3 = ax.text(0.78, 0.75, '', transform=ax.transAxes)

# On subdivise l'array final de fonctions d'onde
psi_anim = psi[::20]

# On définit la fonction à animer qui sera appelée par FuncAnimation
def animate(i):

    this_psi = psi_anim[i]
    line.set_data(x*10**15, abs(this_psi))
    time_text.set_text(time_template % (i*dt*20 * 10**18))
    E_text.set_text(E_template % (energie(k_0, m)*10**(-6)))
    pot_2.set_text(pot_template % (V_0*6.242*10**12))
    return line, time_text

# On appelle la fonction generate_animation pour générer l'animation
file_path = "Projet\/animations\/particule_alpha.mp4"
generate_animation(fig, animate, len(psi_anim), file_path)