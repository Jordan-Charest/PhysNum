import numpy as np
from numpy import pi, exp
import matplotlib.pyplot as plt

# constantes (SI)
hbar = 1.05457182 * 10**(-34)

# paramètres
delta_x = 0.01
x_0 = 0
k_0 = 0
dt = 10
m = 3 * 10**(-31)

# espace 1D
x = np.linspace(-10, 10, 1000)

V = 0

# psi_init = (1 / (2*pi*delta_x**2))**(1/4) * exp(1j*k_0*x - (x-x_0)**2 / (4*delta_x**2))

V = 0

def iteration_temporelle(psi_1, dt):
    phi = exp(-1j*V*dt / (2*hbar)) * psi_1
    phi_fourier = np.fft.fft(phi)
    k = np.fft.fftfreq(len(phi))
    # k = np.fft.fftshift(k)
    # print(k)
    T = hbar**2 * k**2 / (2 * m)
    fourier = exp(-1j*T*dt / (hbar)) * phi_fourier
    fourier_inv = np.fft.ifft(fourier)
    psi_2 = exp(-1j*V*dt / (2*hbar)) * fourier_inv
    return psi_2


def evolution_temporelle(psi_init, N, dt):
    temps = np.linspace(0, N*dt, N)
    psi = [psi_init]
    for i in range(N):
        psi_2 = iteration_temporelle(psi[-1], dt)
        psi.append(psi_2)
    return temps, psi

# def iteration_temporelle(psi_1, dt, t):
#     phi = exp(-1j*V*(t) / (2*hbar)) * psi_1
#     phi_fourier = np.fft.fft(phi)
#     k = np.fft.fftfreq(len(phi))
#     k = np.fft.fftshift(k)
#     # print(k)
#     T = hbar**2 * k**2 / (2 * m)
#     fourier = exp(-1j*T*(t) / (hbar)) * phi_fourier
#     fourier_inv = np.fft.ifft(fourier)
#     psi_2 = exp(-1j*V*(t) / (2*hbar)) * fourier_inv
#     return psi_2


# def evolution_temporelle(psi_init, N, dt):
#     temps = np.linspace(0, N*dt, N)
#     psi = [psi_init]
#     t = 0
#     for i in range(N):
#         t += dt
#         psi_2 = iteration_temporelle(psi_init, dt, t)
#         psi.append(psi_2)
#     return temps, psi

# psi_2 = iteration_temporelle(psi_init, 1)
# iteration_temporelle(psi_2, 1)


# t, psi = evolution_temporelle(psi_init, 1, dt)
# print(psi[0], psi[-1])

# fig1 = plt.figure()
# plt.plot(x, np.absolute(psi[-1]))
# plt.show()