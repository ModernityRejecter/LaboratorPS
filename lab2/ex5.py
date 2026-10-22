import numpy as np
import matplotlib.pyplot as plt
import sounddevice as snd
import scipy

sinus = lambda a, f0, phi, t: a * np.sin(2 * np.pi * f0 * t + phi)

f0 = 400
a = 1
N = 100000
rate = int(44100)

def ex5():
    t = np.linspace(start = 0, stop = 3, num = rate * 3)
    sig1 = sinus(a, f0, 0, t)
    sig2 = sinus(a, 3 * f0, 0, t)
    sig = np.concatenate((sig1, sig2))

    snd.play(sig, rate)
    snd.wait()

# OBSERVATIA CERUTA: sunetul corespunzator primului semnal este mai grav, 
# in schimb, al doilea este considerabil mai acut
ex5()