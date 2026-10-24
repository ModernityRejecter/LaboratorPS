import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import scipy.stats 
import math

sinus = lambda f0, t, phi: np.sin(2 * np.pi * f0 * t + phi)

# figura 1

t1 = np.linspace(start = 0, stop = 1, num = 1000)
f1 = 8
x1 = sinus(f1, t1, np.pi / 2)
y1 = x1 * (math.e ** (-2j * np.pi * t1))
dist_y1 = np.abs(y1)

fig, axs = plt.subplots(1, 2)

axs[0].plot(x1)
axs[1].set_aspect('equal')
axs[1].set_xlim([-1.2, 1.2])
axs[1].set_ylim([-1.2, 1.2])
axs[1].scatter(y1.real, y1.imag, cmap = 'viridis', c = dist_y1, s= 5)

plt.savefig("ex2_fig1.pdf")

# animatie fig 1
fig_anim, axs_anim = plt.subplots(1, 2)
axs_anim[0].set_xlim([0, 1000])
axs_anim[0].set_ylim([-1.2, 1.2])
axs_anim[1].set_aspect('equal')
axs_anim[1].set_xlim([-1.2, 1.2])
axs_anim[1].set_ylim([-1.2, 1.2])


linie_timp, = axs_anim[0].plot([], [])
indicator_timp, = axs_anim[0].plot([], [], 'ro')

scatter_complex = axs_anim[1].scatter([], [], c=[], cmap='viridis', s=5, vmin=0, vmax=np.max(dist_y1))
indicator_complex, = axs_anim[1].plot([], [], 'ro')

def frame_update(i):
    linie_timp.set_data(range(i), x1[:i])
    indicator_timp.set_data([i], [x1[i]])
    
    scatter_complex.set_offsets(np.column_stack((y1[:i].real, y1[:i].imag)))
    scatter_complex.set_array(dist_y1[:i])
    indicator_complex.set_data([y1[i].real], [y1[i].imag])
    
    return linie_timp, indicator_timp, scatter_complex, indicator_complex


anim = FuncAnimation(fig_anim, frame_update, frames=range(0, 1000, 10), interval=30, blit=True)

plt.show()

# figura 2

zw1 = x1 * (math.e ** (-2j * np.pi * t1 * 1))
zw2 = x1 * (math.e ** (-2j * np.pi * t1 * 2))
zw3 = x1 * (math.e ** (-2j * np.pi * t1 * 5))
zw4 = x1 * (math.e ** (-2j * np.pi * t1 * 8))

dist_zw1 = np.abs(zw1)
dist_zw2 = np.abs(zw2)
dist_zw3 = np.abs(zw3)
dist_zw4 = np.abs(zw4)

fig, axs = plt.subplots(2, 2)

for ax in axs.flat:
    ax.set_xlim([-1.2, 1.2])
    ax.set_ylim([-1.2, 1.2])
    ax.set_aspect('equal')
    
axs[0, 0].scatter(zw1.real, zw1.imag, cmap = 'viridis', c = dist_zw1, s= 5)
axs[0, 1].scatter(zw2.real, zw2.imag, cmap = 'viridis', c = dist_zw2, s= 5)
axs[1, 0].scatter(zw3.real, zw3.imag, cmap = 'viridis', c = dist_zw3, s= 5)
axs[1, 1].scatter(zw4.real, zw4.imag, cmap = 'viridis', c = dist_zw4, s= 5)

plt.savefig("ex2_fig2.pdf")

# animatie fig 2
fig_anim2, axs_anim2 = plt.subplots(2, 2)
z_list = [zw1, zw2, zw3, zw4]

scatter_list = []
indicator_list = []

for ax in axs_anim2.flat:
    ax.set_xlim([-1.2, 1.2])
    ax.set_ylim([-1.2, 1.2])
    ax.set_aspect('equal')
    
    sc = ax.scatter([], [], c=[], cmap='viridis', s=5, vmin=0, vmax=np.max(dist_y1))
    ind, = ax.plot([], [], 'ro')
    
    scatter_list.append(sc)
    indicator_list.append(ind)

def frame_update2(i):
    elemente_actualizate = []
    
    for j in range(4):
        z_curent = z_list[j]
        
        scatter_list[j].set_offsets(np.column_stack((z_curent[:i].real, z_curent[:i].imag)))

        scatter_list[j].set_array(dist_y1[:i]) 
        
        indicator_list[j].set_data([z_curent[i].real], [z_curent[i].imag])
        
        elemente_actualizate.extend([scatter_list[j], indicator_list[j]])
        
    return tuple(elemente_actualizate)

anim2 = FuncAnimation(fig_anim2, frame_update2, frames=range(0, 1000, 10), interval=30, blit=True)
plt.show()