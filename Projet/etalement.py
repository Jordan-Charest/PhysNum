from functions import iteration_temporelle, evolution_temporelle, psi_init
import numpy as np
from numpy import pi, exp
import matplotlib.pyplot as plt
import matplotlib.animation as animation


# constantes (SI)
hbar = 1.05457182 * 10**(-34)

# paramètres
delta_x = 5*10**(-10) #1 et 5
x_0 = 0
k_0 = 0
N = 8000 # Nombre de pas
dt = 1 * 10**(-17) # Intervalle de temps
t_max = N*dt # Temps final
m = 3 * 10**(-31)
V = 0
vit = 10 # Vitesse d'animation. 1 = normal, 10 = 10x plus vite

# espace 1D
x = np.linspace(-10*10**(-8), 10*10**(-8), 5000)

psi_init = psi_init(x, x_0, delta_x, k_0)
psi_init = psi_init / np.sqrt((sum(np.abs(psi_init)**2)))

t, psi = evolution_temporelle(psi_init, N, dt, V, m)

fig = plt.figure(figsize=(6, 5))
ax = fig.add_subplot(autoscale_on=True, xlim=(-100, 100), ylim=(0, 0.5))
# ax.set_aspect("equal")
ax.grid()
plt.ylabel("$|ψ|^2$")
plt.xlabel("$x$ [Å]")

line, = ax.plot([], [], "-", lw=1)
time_template = 'temps = %.3f fs'
time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)

# y = np.linspace(-10, 10, 1000)
psi_anim = psi[::20]

def animate(i):
    this_psi = psi_anim[i]

    line.set_data(x*10**10, abs(this_psi))
    # line.set_data(x, x*i/50)
    time_text.set_text(time_template % (i*dt*20 * 10**15))
    return line, time_text

ani = animation.FuncAnimation(fig, animate, len(psi_anim), interval=1, repeat=False)

f = "Projet\/animations\/etalement_test.mp4" 
writervideo = animation.FFMpegWriter(fps=60) 
ani.save(f, writer=writervideo)

#plt.show()

# print(np.array_equal(abs(psi[-1]), abs(psi[-2])))