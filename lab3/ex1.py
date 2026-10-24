import numpy as np
import matplotlib.pyplot as plt
import scipy.stats 
import math
    
N = 8

F = np.zeros((N, N), dtype = complex)
for m in range(N):
    for n in range(N):
        F[m, n] += math.e ** (-2j * np.pi * n * (m / N))
    
fig, axs = plt.subplots(N)

for i, ax in enumerate(axs):
    ax.plot(F[i].real, label ='real')
    ax.plot(F[i].imag, color = 'green', label = 'imaginar' )
    ax.legend(loc = 'upper right')

F_H = F.conj().T
I = np.eye(N) #pentru diagonala

res_norm = (F_H @ F) / N

is_unitary = np.allclose(res_norm, I)

plt.savefig("ex1.pdf")
print(is_unitary)
plt.show()