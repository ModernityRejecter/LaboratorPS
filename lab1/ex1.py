import numpy as np
import matplotlib.pyplot as plt

x = lambda t: np.cos((520 * np.pi * t) + (np.pi / 3))
y = lambda t: np.cos((280 * np.pi * t) - (np.pi / 3))
z = lambda t: np.cos((120 * np.pi * t) + (np.pi / 3))

def sub_a():
    return np.arange(start = 0, stop = 0.03, step = 0.0005)

def sub_b(t):
    xt = x(t)
    yt = y(t)
    zt = z(t)
    fig, axs = plt.subplots(3)
    fig.suptitle("Exercitiul 1b")
    axs[0].plot(t, xt)
    axs[1].plot(t, yt)
    axs[2].plot(t, zt)
    fig.savefig("ex1b.pdf")

def sub_c(t):
    f = 200
    t_stem = np.arange(start = 0, stop = 0.03, step= 1/f)
    fig, axs = plt.subplots(3)
    fig.suptitle("Exercitiul 1c")
    axs[0].plot(t, x(t))
    axs[1].plot(t, y(t))
    axs[2].plot(t, z(t))
    axs[0].stem(t_stem, x(t_stem))
    axs[1].stem(t_stem, y(t_stem))
    axs[2].stem(t_stem, z(t_stem))
    fig.savefig("ex1c.pdf")

timp = sub_a()
sub_b(timp)
sub_c(timp)

plt.show()
