from functions import iteration_temporelle, evolution_temporelle, psi_init
import numpy as np
from numpy import pi, exp
import matplotlib.pyplot as plt
import matplotlib.animation as animation


# constantes (SI)
hbar = 1.05457182 * 10**(-34)

# paramètres
delta_x = 1*10**(-2)
x_0 = 0
k_0 = 2*np.pi / 10**(-10)
N = 5000 # Nombre de pas
dt = 0.01 # Intervalle de temps
t_max = N*dt # Temps final
m = 3 * 10**(-31)
V = 0
vit = 10 # Vitesse d'animation. 1 = normal, 10 = 10x plus vite

# espace 1D
x = np.linspace(-1, 1, 5000)

psi_init = psi_init(x, x_0, delta_x, k_0)
t, psi = evolution_temporelle(psi_init, N, dt, V, m)

fig = plt.figure(figsize=(5, 4))
ax = fig.add_subplot(autoscale_on=True, xlim=(-0.5, 0.5), ylim=(0,10))
# ax.set_aspect("equal")
ax.grid()

line, = ax.plot([], [], "-", lw=1)
time_template = 'temps = %.3fs'
time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)

# y = np.linspace(-10, 10, 1000)

def animate(i):
    this_psi = psi[i]

    line.set_data(x, abs(this_psi))
    # line.set_data(x, x*i/50)
    time_text.set_text(time_template % (i*dt))
    return line, time_text

ani = animation.FuncAnimation(fig, animate, len(psi), interval=1000*dt/vit, repeat=False)
plt.show()

# print(np.array_equal(abs(psi[-1]), abs(psi[-2])))