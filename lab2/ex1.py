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

def ex1():
    t = np.linspace(start = 0, stop = 1, num = N)
    fig, axs = plt.subplots(2)
    fig.suptitle("Exercitiul 1")

    axs[0].plot(t, sinus(a, f0, 0, t))
    axs[0].set_xlim(0, 1/400)

    axs[1].plot(t, cosinus(a, f0, 3 * np.pi / 2, t))
    axs[1].set_xlim(0, 1/400)

    plt.savefig("ex1.pdf")
    plt.show()

ex1()