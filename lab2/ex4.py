import numpy as np
import matplotlib.pyplot as plt
import sounddevice as snd
import scipy

sinus = lambda a, f0, phi, t: a * np.sin(2 * np.pi * f0 * t + phi)
sawtooth = lambda t, f0, mod: np.mod(f0 * t, mod)

f0 = 400
a = 1
N = 100000

def ex4():
    t = np.linspace(start = 0, stop = 1, num = N)
    sin = sinus(a, f0, 0, t)
    saw = sawtooth(t, f0, a)
    sinsaw = sin + saw

    fig, axs = plt.subplots(3)
    fig.suptitle("Sinusoida + Sawtooth")

    axs[0].plot(t, sin)
    axs[1].plot(t, saw)
    axs[2].plot(t, sinsaw)

    for ax in axs:
        ax.set_xlim(0, 1/100)

    plt.savefig("ex4.pdf")
    plt.show()

ex4()