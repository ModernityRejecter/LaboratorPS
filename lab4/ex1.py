import numpy as np
import matplotlib.pyplot as plt
import math
import time

def dft(x):
    N = len(x)

    F = np.zeros((N, N), dtype = complex)
    
    for m in range(N):
        for n in range(N):
            F[m, n] = np.exp(-2j * np.pi * m * n / N)
            
    return F @ x

def fft(x):
    N = len(x)
    
    if N > 1:  
        x_even = fft(x[::2]) 
        x_odd = fft(x[1::2])

        X = np.zeros(N, dtype = complex)
        
        for k in range(N // 2):
            xk = np.exp(-2j * np.pi * k / N)
            
            X[k] = x_even[k] + xk * x_odd[k]
            X[N // 2 + k] = x_even[k] - xk * x_odd[k]

        return X
    
    else:
        return x
    
elapsed_time_custom_fft = []
elapsed_time_np_fft = []
elapsed_time_custom_dft = []

powers = range(7, 14)
sizes = [2 ** i for i in powers]

np.fft.fft(np.array([1.0, 2.0])) # warmup pentru np.fft

for N in sizes: 
    x = np.linspace(0, 1, num = N)
    
    ## fft custom
    start_time = time.time()
    fft(x)
    end_time = time.time()
    
    elapsed_time_custom_fft.append(end_time - start_time)
    
    ## np fft
    start_time = time.perf_counter()
    np.fft.fft(x)
    end_time = time.perf_counter()
    
    elapsed_time_np_fft.append(end_time - start_time)
    
    ## dft custom
    start_time = time.time()
    dft(x)
    end_time = time.time()
    
    elapsed_time_custom_dft.append(end_time - start_time)
    
plt.figure()
plt.title("Custom FFT vs NumPy FFT vs Custom DFT")
plt.plot(sizes, elapsed_time_custom_fft, label = "Custom FFT")
plt.plot(sizes, elapsed_time_np_fft, label = "NumPy FFT")
plt.plot(sizes, elapsed_time_custom_dft, label = "Custom DFT")
plt.legend()
plt.xlabel("N")
plt.ylabel("Timp (secunde)")
plt.yscale('log')
plt.savefig("ex1.pdf")
plt.show()