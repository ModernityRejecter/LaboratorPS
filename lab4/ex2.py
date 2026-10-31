import numpy as np
import matplotlib.pyplot as plt
import math
import time

sinus = lambda f0, t, phi: np.sin(2 * np.pi * f0 * t + phi)

sub_nyq_f = 340

f1 = 300
f2 = f1 + sub_nyq_f
f3 = f1 - sub_nyq_f # -40, sin(-x) = -sin(x) 

t = np.linspace(0, 1, num = 100000)
sub_nyq_t = np.linspace(0, 1, num = sub_nyq_f)

x1 = sinus(f1, t, 0)
x2 = sinus(f2, t, 0)
x3 = sinus(f3, t, 0)

sub_nyq_x1 = sinus(f1, sub_nyq_t, 0)
sub_nyq_x2 = sinus(f2, sub_nyq_t, 0)
sub_nyq_x3 = sinus(f3, sub_nyq_t, 0)

fig, axs = plt.subplots(4, figsize = (12, 8))

for ax in axs:
    ax.set_xlim(0, 6 * (1 / f1))
    
axs[0].plot(t, x1, color = 'red')

axs[1].plot(t, x1, color = 'orange', zorder = 1)
axs[1].scatter(sub_nyq_t, sub_nyq_x1, zorder = 2)

axs[2].plot(t, x2, color = 'gold', zorder = 1)
axs[2].scatter(sub_nyq_t, sub_nyq_x2, zorder = 2)

axs[3].plot(t, x3, color = 'greenyellow', zorder = 1)
axs[3].scatter(sub_nyq_t, sub_nyq_x3, zorder = 2)

plt.savefig("ex2.pdf")
plt.show()