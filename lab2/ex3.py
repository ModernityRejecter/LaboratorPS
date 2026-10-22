import numpy as np
import matplotlib.pyplot as plt
import sounddevice as snd
import scipy

# functiile de la ex 2 a-d de la laboratorul anterior
# am modificat durata la 3 secunde pentru aproape toate semnalele

x = lambda A, t, phi, f0: A * np.sin(2 * np.pi * f0 * t + phi)
sawtooth = lambda t, f0, mod: np.mod(f0 * t, mod)
square = lambda t, f0: np.sign(x(1, t, 0, f0))

rate = int(44100)

def sub_a():

    f0 = 400
    phi = 3.15
    A = 1
    t = np.linspace(start = 0, stop = 3, num = rate * 3)

    return t, x(A, t, phi, f0)

ta, xta = sub_a()

def sub_b():
    f0 = 800
    phi = 3.15
    A = 1
    t = np.linspace(start= 0, stop = 3, num = rate * 3)

    return t, x(A, t, phi, f0)

tb, xtb = sub_b()

def sub_c():
    
    f0 = 240
    A = 1
    t = np.linspace(start = 0, stop = 3, num = rate * 3)

    return t, sawtooth(t, f0, A)

tc, xtc = sub_c()

def sub_d():

    f0 = 300
    t = np.linspace(start = 0, stop = 3, num = rate * 3)

    return t, square(t, f0)

td, xtd = sub_d()

def ex3():

    f0 = 400
    phi = 3.15
    A = 1
    t = np.linspace(start = 0, stop = 3, num = rate * 3)

    _, sound_a = sub_a()
    _, sound_b = sub_b()
    _, sound_c = sub_c()
    _, sound_d = sub_d()

    snd.play(sound_a, rate)
    snd.wait()
    snd.play(sound_b, rate)
    snd.wait()
    snd.play(sound_c, rate)
    snd.wait()
    snd.play(sound_d, rate)
    snd.wait()

    scipy.io.wavfile.write("ex3.wav", rate, x(A, t, phi, f0))
    rate_read, myarray = scipy.io.wavfile.read("ex3.wav")
    snd.play(myarray, rate_read)
    snd.wait()

ex3()