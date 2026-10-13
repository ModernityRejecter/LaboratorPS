import numpy as np
import matplotlib.pyplot as plt


x = lambda A, t, phi, f0: A * np.sin(2 * np.pi * f0 * t + phi)
sawtooth = lambda t, f0, mod: np.mod(f0 * t, mod)
square = lambda t, f0: np.sign(x(1, t, 0, f0))

def sub_a():

    f0 = 400
    phi = 3.15
    A = 1
    t = np.linspace(start = 0, stop = 0.03, num = 1600)

    return t, x(A, t, phi, f0)

ta, xta = sub_a()

def sub_b():
    f0 = 800
    phi = 3.15
    A = 1
    t = np.linspace(start= 0, stop = 3, num = 250000)

    return t, x(A, t, phi, f0)

tb, xtb = sub_b()

def sub_c():
    
    f0 = 240
    A = 1
    t = np.linspace(start = 0, stop = 0.03, num = 5000)

    return t, sawtooth(t, f0, A)

tc, xtc = sub_c()

def sub_d():

    f0 = 300
    t = np.linspace(start = 0, stop = 0.03, num = 10000)

    return t, square(t, f0)

td, xtd = sub_d()

def sub_e():

    canvas = np.random.rand(128, 128)
    return canvas

ex2_e = sub_e()

def sub_f():

    canvas = np.zeros((128, 128))

    canvas[44:56, 28:30] = 1  # verticala stanga
    canvas[44:56, 32:34] = 1  # verticala dreapta
    canvas[54:56, 30:32] = 1  # bara jos

    # --- 'n' (coloanele 36:42) ---
    canvas[44:56, 36:38] = 1  # verticala stanga
    canvas[44:56, 40:42] = 1  # verticala dreapta
    canvas[44:46, 38:40] = 1  # bara sus

    # [spatiu] (coloanele 42:50)

    # --- 'p' (coloanele 50:56) ---
    canvas[44:56, 50:52] = 1  # verticala stanga
    canvas[44:46, 52:56] = 1  # bara sus
    canvas[49:51, 52:56] = 1  # bara mijloc
    canvas[44:51, 54:56] = 1  # verticala dreapta sus

    # --- 'a' (coloanele 58:64) ---
    canvas[44:56, 58:60] = 1  # verticala stanga
    canvas[44:56, 62:64] = 1  # verticala dreapta
    canvas[44:46, 60:62] = 1  # bara sus
    canvas[49:51, 60:62] = 1  # bara mijloc

    # --- 'r' (coloanele 66:72) --- piciorus oblic modificat
    canvas[44:56, 66:68] = 1  # verticala stanga
    canvas[44:46, 68:72] = 1  # bara sus
    canvas[49:51, 68:71] = 1  # bara mijloc
    canvas[44:50, 70:72] = 1  # bucla dreapta sus
    canvas[50:53, 68:70] = 1  # piciorus oblic sus (retras spre stanga)
    canvas[53:56, 70:72] = 1  # piciorus oblic jos (spre dreapta)

    # --- 'i' (coloanele 74:76) ---
    canvas[44:56, 74:76] = 1  # bara verticala

    # --- 'n' (coloanele 78:84) ---
    canvas[44:56, 78:80] = 1  # verticala stanga
    canvas[44:56, 82:84] = 1  # verticala dreapta
    canvas[44:46, 80:82] = 1  # bara sus

    # --- 't' (coloanele 86:92) ---
    canvas[44:46, 86:92] = 1  # bara sus
    canvas[46:56, 88:90] = 1  # verticala mijloc

    # --- 'e' (coloanele 94:100) ---
    canvas[44:56, 94:96] = 1   # verticala stanga
    canvas[44:46, 96:100] = 1  # bara sus
    canvas[49:51, 96:99] = 1   # bara mijloc
    canvas[54:56, 96:100] = 1  # bara jos


    # =========================================================
    # LINIA 2: "responsabil ..." (pe liniile 68:80)
    # =========================================================

    # --- 'r' (coloanele 15:21) --- piciorus oblic modificat
    canvas[68:80, 15:17] = 1  # verticala stanga
    canvas[68:70, 17:21] = 1  # bara sus
    canvas[73:75, 17:20] = 1  # bara mijloc
    canvas[68:74, 19:21] = 1  # bucla dreapta sus
    canvas[74:77, 17:19] = 1  # piciorus oblic sus (retras spre stanga)
    canvas[77:80, 19:21] = 1  # piciorus oblic jos (spre dreapta)

    # --- 'e' (coloanele 23:29) ---
    canvas[68:80, 23:25] = 1  # verticala stanga
    canvas[68:70, 25:29] = 1  # bara sus
    canvas[73:75, 25:28] = 1  # bara mijloc
    canvas[78:80, 25:29] = 1  # bara jos

    # --- 's' (coloanele 31:37) ---
    canvas[68:70, 31:37] = 1  # bara sus
    canvas[70:73, 31:33] = 1  # colt stanga sus
    canvas[73:75, 31:37] = 1  # bara mijloc
    canvas[75:78, 35:37] = 1  # colt dreapta jos
    canvas[78:80, 31:37] = 1  # bara jos

    # --- 'p' (coloanele 39:45) ---
    canvas[68:80, 39:41] = 1  # verticala stanga
    canvas[68:70, 41:45] = 1  # bara sus
    canvas[73:75, 41:45] = 1  # bara mijloc
    canvas[68:75, 43:45] = 1  # verticala dreapta sus

    # --- 'o' (coloanele 47:53) ---
    canvas[68:80, 47:49] = 1  # verticala stanga
    canvas[68:80, 51:53] = 1  # verticala dreapta
    canvas[68:70, 49:51] = 1  # bara sus
    canvas[78:80, 49:51] = 1  # bara jos

    # --- 'n' (coloanele 55:61) ---
    canvas[68:80, 55:57] = 1  # verticala stanga
    canvas[68:80, 59:61] = 1  # verticala dreapta
    canvas[68:70, 57:59] = 1  # bara sus

    # --- 's' (coloanele 63:69) ---
    canvas[68:70, 63:69] = 1  # bara sus
    canvas[70:73, 63:65] = 1  # colt stanga sus
    canvas[73:75, 63:69] = 1  # bara mijloc
    canvas[75:78, 67:69] = 1  # colt dreapta jos
    canvas[78:80, 63:69] = 1  # bara jos

    # --- 'a' (coloanele 71:77) ---
    canvas[68:80, 71:73] = 1  # verticala stanga
    canvas[68:80, 75:77] = 1  # verticala dreapta
    canvas[68:70, 73:75] = 1  # bara sus
    canvas[73:75, 73:75] = 1  # bara mijloc

    # --- 'b' (coloanele 79:85) ---
    canvas[68:80, 79:81] = 1  # verticala stanga
    canvas[68:70, 81:84] = 1  # bara sus
    canvas[73:75, 81:84] = 1  # bara mijloc
    canvas[78:80, 81:84] = 1  # bara jos
    canvas[70:73, 83:85] = 1  # colt dreapta sus
    canvas[75:78, 83:85] = 1  # colt dreapta jos

    # --- 'i' (coloanele 87:89) ---
    canvas[68:80, 87:89] = 1  # bara verticala

    # --- 'l' (coloanele 91:96) ---
    canvas[68:80, 91:93] = 1  # verticala stanga
    canvas[78:80, 93:96] = 1  # talpa jos

    # [spatiu] (coloanele 96:104)

    # --- '.' primul punct (coloanele 104:106) ---
    canvas[78:80, 104:106] = 1

    # --- '.' al doilea punct (coloanele 108:110) ---
    canvas[78:80, 108:110] = 1

    # --- '.' al treilea punct (coloanele 112:114) ---
    canvas[78:80, 112:114] = 1  

    return canvas

ex2_f = sub_f()

plt.figure()
plt.title("Exercitiul 2a")
plt.stem(ta, xta)
plt.xlim(0, 1/400)
plt.savefig("ex2a.pdf")
plt.show()

plt.figure()
plt.title("Exercitiul 2b")
plt.plot(tb, xtb)
plt.xlim(0, 1/200)
plt.savefig("ex2b.pdf")
plt.show()

plt.figure()
plt.title("Exercitiul 2c")
plt.plot(tc, xtc)
plt.xlim(0, 1/60)
plt.savefig("ex2c.pdf")
plt.show()

plt.figure()
plt.title("Exercitiul 2d")
plt.plot(td, xtd)
plt.xlim(0, 1/100)
plt.savefig("ex2d.pdf")
plt.show()

plt.figure()
plt.title("Exercitiul 2e")
plt.imshow(ex2_e)
plt.savefig("ex2e.pdf")
plt.show()

plt.figure()
plt.title("Exercitiul 2f")
plt.imshow(ex2_f)
plt.savefig("ex2f.pdf")
plt.show()