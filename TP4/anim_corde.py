import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, FFMpegWriter


def corde_FTCS(phi_0, psi_0, L, N, t_f, N_t, v):
    # pas temporel et spatial
    h = t_f / N_t
    a = L / N
    
    # variables indépendantes
    t = np.linspace(0, t_f, N_t)
    x = np.linspace(0, L, N)

    # valeurs initiales en listes
    phi = [list(phi_0)]
    psi = [list(psi_0)]

    # processus itératif en listes (zéro au début et à la fin pour les bouts fixes)
    for i in range(len(t)):
        psi_i = [0]
        phi_i = [0]
        for j in range(len(x))[1:-1]:
            phi_j = phi[i][j] + h*psi[i][j]
            psi_j = psi[i][j] + h*v**2/a**2 * (phi[i][j+1] + phi[i][j-1] - 2*phi[i][j])
            phi_i.append(phi_j)
            psi_i.append(psi_j)
        phi_i.append(0)
        psi_i.append(0)
        phi.append(phi_i)
        psi.append(psi_i)
    
    # conversion en array
    return t, np.array(phi), np.array(psi)


# données
L = 1
N = 100
t_f = 0.1
h = 10**(-6)
N_t = int(t_f / h)
C = 1
d = 0.1
sigma = 0.3
v = 100

# conditions initiales
init_phi = np.zeros(N)
x = np.linspace(0, L, N)
init_psi = C*x*(L-x) / L**2 * np.exp(-(x-d)**2 / (2*sigma**2))

t, phi, psi = corde_FTCS(init_phi, init_psi, L, N, t_f, N_t, v)


# création de la figure et la ligne qui contiendra les données
fig2 = plt.figure(figsize=(10,2))
fig2.patch.set_facecolor('white')
ax = plt.axes(xlim=(0, 1), ylim=(-0.001, 0.001))
line, = ax.plot([], [], lw=2)
plt.xlabel("x [m]")
plt.ylabel("$\phi$ [m]")
plt.title("Position de la corde de 0 à 100 ms")

# 1 frame pour 100 itérations temporelles
phi_anim = phi[::200]
psi_anim = psi[::200]

# fonction d'initialisation
def fonc_init():
    line.set_data([], [])
    return line,

# fonction d'animation
def anim(i):
    x = np.linspace(0, 1, 100)
    y = phi_anim[i]
    line.set_data(x, y)
    return line,

# animation
corde1 = FuncAnimation(fig2, anim, init_func=fonc_init, frames=500, interval=10, repeat=True)

# sauvegarde
writervideo = FFMpegWriter(fps=30)
corde1.save("corde1.mp4", writer=writervideo)

plt.show()