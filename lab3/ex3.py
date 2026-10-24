import numpy as np
import matplotlib.pyplot as plt
import scipy.stats 
import math

N = 1000

F = np.zeros((N, N), dtype = complex)
for m in range(N):
    for n in range(N):
        F[m, n] += math.e ** (-2j * np.pi * n * (m / N))
        
sinus = lambda f0, t, phi = 0: np.sin(2 * np.pi * f0 * t + phi)
t = np.arange(start = 0, stop = 1, step = 1/N)
f1, f2, f3 = 5, 16, 73
x_comp = sinus(f1, t) + sinus(f2, t) + sinus(f3, t)

x_res = F @ x_comp

fig, axs = plt.subplots(2, 1)
    
axs[0].plot(t, x_comp)
axs[1].stem(np.abs(x_res))
axs[1].set_xlim([0, 99])

plt.savefig("ex3.pdf")
plt.show()