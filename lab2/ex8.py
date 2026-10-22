import numpy as np
import matplotlib.pyplot as plt
import sounddevice as snd
import scipy

def ex8():

    alpha = np.linspace(-np.pi/2, np.pi/2, 1000)
    
    sin_real = np.sin(alpha)
    taylor = alpha
    pade = (alpha - (7 * alpha**3) / 60) / (1 + (alpha**2) / 20)

    eroare_taylor = np.abs(sin_real - taylor)
    eroare_pade = np.abs(sin_real - pade)
    
    fig, axs = plt.subplots(3, 1, figsize=(8, 10))
    
    axs[0].plot(alpha, sin_real, label="sin(alpha)", color="blue", linewidth=2)
    axs[0].plot(alpha, taylor, label="Taylor", linestyle="--", color="orange")
    axs[0].plot(alpha, pade, label="Pade", linestyle="-.", color="green")
    axs[0].set_title("Comparatie Functii")
    axs[0].legend()
    
    axs[1].plot(alpha, eroare_taylor, label="Eroare Taylor", color="orange")
    axs[1].plot(alpha, eroare_pade, label="Eroare Pade", color="green")
    axs[1].set_title("Eroare absoluta")
    axs[1].legend()
    
    axs[2].plot(alpha, eroare_taylor, label="Eroare Taylor", color="orange")
    axs[2].plot(alpha, eroare_pade, label="Eroare Pade", color="green")
    axs[2].set_title("Eroare absoluta pe scara logaritmica")
    axs[2].set_yscale('log')
    axs[2].legend()
    
    plt.tight_layout()
    plt.savefig("ex8.pdf")
    plt.show()

ex8()