from functions import iteration_temporelle, evolution_temporelle, evolution_temporelle_alpha, psi_init, energie
import numpy as np
from numpy import pi, exp
import matplotlib.pyplot as plt
import matplotlib.animation as animation


# constantes (SI)
hbar = 1.05457182 * 10**(-34)
h = 6.62607015 * 10**(-34)
c = 299792458

# paramètres
delta_x = 0.1*10**(-15)
x_0 = -3 * 10**(-15)
k_0 = 9.7835 * 10 ** 14
N = 8000 # Nombre de pas
dt = 0.5 * 10**(-23) # Intervalle de temps
t_max = N*dt # Temps final
m = 6.644 * 10**(-27)
V_0 = -1804.232 * 10**6 / (6.242*10**18) # puits de pot en J
V_1 = 4.615 * 10**(-26) # Potentiel coulombien * r
vit = 10 # Vitesse d'animation. 1 = normal, 10 = 10x plus vite
r = 1.2*10**(-15) * 238**(1/3) # Rayon approx d'un noyau d'Uranium 238
Nb = 5000
# Selon le potentiel coulombien, la particule devrait faire un effet tunnel à environ x = 57,6 fm

# espace 1D
x = np.linspace(-200*10**(-15), 200*10**(-15), Nb)

# potentiel
V_liste = []
for i in x:
    if abs(i) < r:
        V_liste.append(V_0)
    else:
        V_liste.append(V_1/abs(i))
V = np.array(V_liste)

psi_init = psi_init(x, x_0, delta_x, k_0)
psi_init = psi_init / np.sqrt((sum(np.abs(psi_init)**2))*400*10**(-15)/Nb)

t, psi = evolution_temporelle_alpha(psi_init, N, Nb, dt, V, m)

fig = plt.figure(figsize=(6, 5))
ax = fig.add_subplot(autoscale_on=True, xlim=(-200, 200), ylim=(0, 4*10**7))
# ax.set_aspect("equal")
ax.grid()
plt.axvline(x=-r*10**(15), color="black")
plt.axvline(x=r*10**(15), color="black")
plt.ylabel("$|ψ|^2$")
plt.xlabel("$x$ [fm]")

line, = ax.plot([], [], "-", lw=1)
time_template = 'temps = %.3f as'
pot_template = "V = %.3f eV"
E_template = "E = %.3f eV"
time_text = ax.text(0.03, 0.9, '', transform=ax.transAxes)
E_text = ax.text(0.03, 0.85, '', transform=ax.transAxes)
pot_1 = ax.text(0.03, 0.75, '', transform=ax.transAxes)
pot_2 = ax.text(0.38, 0.75, '', transform=ax.transAxes)
pot_3 = ax.text(0.78, 0.75, '', transform=ax.transAxes)

# y = np.linspace(-10, 10, 1000)

psi_anim = psi[::20]

def animate(i):
    this_psi = psi_anim[i]

    line.set_data(x*10**15, abs(this_psi))
    # line.set_data(x, x*i/50)
    time_text.set_text(time_template % (i*dt*20 * 10**18))
    E_text.set_text(E_template % (energie(k_0, m)))
    # pot_1.set_text(pot_template % (0))
    pot_2.set_text(pot_template % (V_0*6.242*10**18))
    # pot_3.set_text(pot_template % (0))
    return line, time_text

ani = animation.FuncAnimation(fig, animate, len(psi_anim), interval=1, repeat=False)

f = "Projet\/animations\/alpha_50k_test.mp4" 
writervideo = animation.FFMpegWriter(fps=60) 
ani.save(f, writer=writervideo)

# plt.show()


# détermination de R et T
# R = []
# T = []

# psi_apres = psi[4000]
# R = sum(np.abs(psi_apres[:2500]))
# T = sum(np.abs(psi_apres[2500:]))

# print(R/(R+T), T/(R+T))