import numpy as np
import matplotlib.pyplot as plt
import sounddevice as snd
import scipy
import math
import time

# a)
fs, signal = scipy.io.wavfile.read("audio.wav")
signal = signal[:, 0] # audio-ul original e dual channel
N = len(signal)

grouped_signal = []
n = int(N * 0.01)
nr_groups = N // n
step= int(n // 2)

# b)
for i in range(0, N - n + 1, step):
    grouped_signal.append(signal[i : i + n])
    
# c)
group_fft = []
for group in grouped_signal:
    group_fft.append(np.fft.fft(group))

# d) 
group_fft_abs = np.abs(group_fft).T # tranpusa ca sa devina coloane

# e)
plt.figure()
plt.imshow(10 * np.log10(group_fft_abs + 1e-10), aspect = 'auto', origin = 'lower', cmap = 'plasma')
plt.savefig("ex6.pdf")
plt.show()