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

def ex6():
    t = np.arange(start = 0, stop = 1, step = 1/N)
    f1 = N / 2
    f2 = N / 4
    f3 = 0

    fig, axs = plt.subplots(3)
    fig.suptitle("f1, f2, f3")

    axs[0].plot(t, sinus(a, f1, 0, t))
    axs[1].plot(t, sinus(a, f2, 0, t))
    axs[2].plot(t, sinus(a, f3, 0, t))

    for ax in axs:
        ax.set_xlim(0, 1 /(f2 / 16))

    plt.savefig("ex6.pdf")
    plt.show()

# Pentru f = fs / 2: functia devine 1 * np.sin(2 * np.pi * fs/2 * t + 0), esantionam de 2 ori intr-o faza, la 0 si pi unde valorile sunt 0 si 0 astfel vedem o linie dreapta
# Pentru f = fs / 4: functia devine 1 * np.sin(2 * np.pi * fs/4 * t + 0), esantionam de 4 ori intr-o faza, astfel vom prinde valorile la 0, 1, 0 si -1
# Pentru f = 0 Hz: functia devine 1 * np.sin(2 * np.pi * 0 * t + 0) adica np.sin(0) deci 0 in toate punctele, astfel ramane o linie dreapta

ex6()