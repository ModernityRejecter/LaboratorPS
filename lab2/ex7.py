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

def ex7():
    t1 = np.linspace(start = 0, stop = 1, num = 20000)
    t2 = t1[::4]
    t3 = t1[1::4]
    sin1 = sinus(a, f0, 0, t1)
    sin2 = sin1[::4]
    sin3 = sin1[1::4]
 
    fig, axs = plt.subplots(3)
    fig.suptitle("Reductie 1/4 a sinusoidei")

    axs[0].stem(t1, sin1)
    axs[1].stem(t2, sin2)
    axs[2].stem(t3, sin3)

    for ax in axs:
        ax.set_xlim(0, (1 / f0) * 3)

    plt.savefig("ex7.pdf")
    plt.show()

    # a) frecventa de esantionare este redusa la un sfert, astfel graficul isi pierde din rezolutie
    # b) semnalul este acelasi, dar diferenta observabila este decalarea la dreapta putin pe axa timpului,
    # din cauza timpului de inceput dat de t3 care porneste de la indicele 1 in loc de 0
ex7()