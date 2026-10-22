import numpy as np
import matplotlib.pyplot as plt
import sounddevice as snd
import scipy

sinus = lambda a, f0, phi, t: a * np.sin(2 * np.pi * f0 * t + phi)
cosinus = lambda a, f0, phi, t: a * np.cos(2 * np.pi * f0 * t + phi)
sawtooth = lambda t, f0, mod: np.mod(f0 * t, mod)
x = lambda A, t, phi, f0: A * np.sin(2 * np.pi * f0 * t + phi)

f0 = 400
a = 1
N = 100000
gamma = 0

def ex2():
    t = np.linspace(start = 0, stop = 1, num = N)
    xn = sinus(a, f0, 0, t)
    zn = np.random.normal(size = N)

    gamma = lambda c, xn, zn: np.sqrt(c * np.pow(np.linalg.norm(xn), 2) / (np.pow(np.linalg.norm(zn), 2)))

    # SNR = np.sqrt(np.pow(np.linalg.norm(xn), 2) / (np.pow(gamma, 2) * np.pow(np.linalg.norm(zn), 2)))

    plt.figure()
    
    plt.plot(t, sinus(a, f0, 0, t))
    plt.plot(t, sinus(a, f0, np.pi / 2, t))
    plt.plot(t, sinus(a, f0, np. pi, t))
    plt.plot(t, sinus(a, f0, 3 * np.pi / 2, t))
    plt.xlim(0, 1/400)

    plt.savefig("ex2a.pdf")
    plt.show()

    fig, axs = plt.subplots(4)
    fig.suptitle("Zgomot = {0.1, 1, 10, 100}")

    axs[0].plot(t, sinus(a, f0, 0, t) + gamma(1 / 0.1, xn, zn) * zn)
    axs[1].plot(t, sinus(a, f0, 0, t) + gamma(1 / 1, xn, zn) * zn)
    axs[2].plot(t, sinus(a, f0, 0, t) + gamma(1 / 10, xn, zn) * zn)
    axs[3].plot(t, sinus(a, f0, 0, t) + gamma(1 / 100, xn, zn) * zn)

    for ax in axs:
        ax.set_xlim(0, 1/100)

    plt.savefig("ex2b.pdf")
    plt.show()

ex2()