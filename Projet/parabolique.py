from functions import iteration_temporelle, evolution_temporelle, psi_init
import numpy as np
from numpy import pi, exp
import matplotlib.pyplot as plt
import matplotlib.animation as animation


# constantes (SI)
hbar = 1.05457182 * 10**(-34)

# paramètres
delta_x = 1*10**(-10)
x_0 = 0
k_0 = 5 * 10 ** 10 # 1 et 5
N = 8000 # Nombre de pas
dt = 1 * 10**(-17) # Intervalle de temps
t_max = N*dt # Temps final
m = 3 * 10**(-31)
omega = 1 * 10 ** 15
vit = 10 # Vitesse d'animation. 1 = normal, 10 = 10x plus vite

# espace 1D
x = np.linspace(-10*10**(-8), 10*10**(-8), 5000)

# potentiel
V = 1/2 * m * omega**2 * x**2

psi_init = psi_init(x, x_0, delta_x, k_0)
psi_init = psi_init / np.sqrt((sum(np.abs(psi_init)**2)))

t, psi = evolution_temporelle(psi_init, N, dt, V, m)

fig = plt.figure(figsize=(6, 5))
ax = fig.add_subplot(autoscale_on=True, xlim=(-100, 100), ylim=(0, 0.5))
# ax.set_aspect("equal")
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


# y = np.linspace(-10, 10, 1000)

psi_anim = psi[::20]

def animate(i):
    this_psi = psi_anim[i]

    line.set_data(x*10**10, abs(this_psi))
    line2.set_data(x*10**10, V)
    # line.set_data(x, x*i/50)
    time_text.set_text(time_template % (i*dt*20 * 10**15))
    pot_1.set_text(pot_template)
    return line, time_text

ani = animation.FuncAnimation(fig, animate, len(psi_anim), interval=1, repeat=False)

# f = "Projet\/animations\/parabolique_2.mp4" 
# writervideo = animation.FFMpegWriter(fps=60) 
# ani.save(f, writer=writervideo)

# plt.show()


# détermination de R et T
# R = []
# T = []

# psi_apres = psi[4000]
# R = sum(np.abs(psi_apres[:2500]))
# T = sum(np.abs(psi_apres[2500:]))

# print(R/(R+T), T/(R+T))