import matplotlib.pyplot as plt
import numpy as np

x = np.genfromtxt("Train.csv", delimiter=',', skip_header = 1, usecols = 2)
N = len(x)

x_copy = x.copy()

# exercitiul 1a 

Fs =  1 / 3600 # 3600 secunde intr-o ora, se esantinoeaza din ora in ora deci o data la 3600 secunde

# exercitiul 1b

# avem 18288 esantioane, deci 18288 ore => 18288 / 24 zile => 762 zile

# exercitiul 1c

# Teorema Nyquist-Shannon ne spune ca frecventa de esantionare trebuie sa fie cel putin dubla frecventei maxime astfel incat sa
# nu existe fenomenul de aliere, adica Fs > 2 * Fmax. Pentru frecventa de esantionare Fs = 1 / 3600 rezulta:
# 1 / 3600 = 2 * Fmax => 1 / 7200 = Fmax

# exercitiul 1d 
fft_x = np.fft.fft(x)
fft_x = np.abs(fft_x / N)
fft_x = fft_x[:N // 2]
f = Fs * np.linspace(0, N // 2, N // 2) / N

plt.figure()
plt.xlabel("Frecventa (Hz)")
plt.ylabel("|fft_x|")
plt.plot(f, fft_x, color = "green")
plt.scatter(f, fft_x, color = "lime", zorder = 2)
plt.savefig("ex1d.pdf")
plt.show()

# exercitiul 1e 
# exista o componenta continua care se poate observa la frecventa 0 Hz in grafic, aceasta fiind media semnalului

x = x - np.mean(x)
fft_x = np.fft.fft(x)
fft_x = np.abs(fft_x / N)
fft_x = fft_x[:N // 2]

plt.figure()
plt.xlabel("Frecventa (Hz)")
plt.ylabel("|fft_x|")
plt.plot(f, fft_x, color = "green")
plt.scatter(f, fft_x, color = "lime", zorder = 2)
plt.savefig("ex1e.pdf")
plt.show()

# exercitiul 1f
top4 = np.argsort(fft_x)
top4 = top4[-4:]
for i, idx in enumerate(top4):
    print(f"top {i + 1}: |fft_x| = {fft_x[idx]}, f = {f[idx]}, T = {(Fs / f[idx] / 24)}") # T este perioada in zile

# top 1 -> ~253 adica in jur de 8 luni
# top 2 -> ~1 adica o zi exact, trafic mare ziua, mai mic noaptea
# top 3 -> ~380 -> ~1 an, influentat de anotimpuri
# top 4 -> ~761 adica toata durata esantionarii, aproximativ 2 ani

# exercitiul 1g
start_g = 6960 #6960 % 24 = 0, 6960 este ora 00:00 pentru o zi de luni, am tras concluzia ca este luni uitandu-ma pe grafic
end_g = start_g + 31 * 24
t = np.arange(start = start_g, stop = end_g)
plt.figure()
plt.xlabel("Esantioane (ore)")
plt.ylabel("Nr masini")
plt.plot(t, x_copy[start_g : end_g])
plt.savefig("ex1g.pdf")
plt.show()

# exercitiul 1h

# pentru a determina ziua saptamanii in care a inceput masurarea semnalului am putea sa ne bazam pe faptul ca intr-o masura,
# semnalul ar trebui sa fie cat de cat periodic la 7 zile, astfel putem afla prima perioada intreaga, si in functie de aceasta sa 
# determinam ziua saptamanii in care s-a inceput. In mod normal traficul ar trebui sa fie mai elevat in timpul saptamanii fata de
# weekend ceea ce ne-ar permite sa identificam corect o perioada.
# Deoarece semnalul este si periodic zilnic putem deduce si ora asumand ca pe timp de noapte traficul trebuie sa fie mai mic
# Pentru data exacta ne putem folosi de distantele de timp dintre esantioane unde traficul este abnormal de mic pentru zile
# normale ale saptamanii, putem astfel presupune ca sunt sarbatori si calculand timpul intre acestea sa determinam si despre ce sarbatori
# este vorba. Tot aceasta abordare aduce o problema, exista posibilitatea ca un trafic abnormal sa nu fie cauzat de o sarbatoare ci
# de un eveniment care nu are nicio relevanta sau legatura cu o anumita data calendaristica, spre exemplu un concert, accident mare
# la nivel de oras, etc.


# exercitiul 1i

# Eliminam componentele de frecventa inalta, permitand doar fenomene cu perioada >= 4 saptamani (28 zile = 672 ore).
# pracitc eliminam zgomotul orar, spike-urile, ciclul zilnic si variatiile de weekend,
# pastrand doar evolutia generala a traficului.


X = np.fft.fft(x_copy)
k = N // (4 * 7 * 24)
X[k : N - k] = 0
x_filtered = np.fft.ifft(X).real

plt.figure()
plt.plot(t, x_copy[start_g : end_g], label = "Semnal brut", alpha = 0.6)
plt.plot(t, x_filtered[start_g : end_g], label = "Semnal filtrat", color = "red", linewidth = 2)
plt.xlabel("Esantioane (ore)")
plt.ylabel("Nr masini")
plt.legend()
plt.savefig("ex1i.pdf")
plt.show()