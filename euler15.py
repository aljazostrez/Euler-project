from math import factorial

# Število vseh potez = 40
# Število zasukov v desno = 20

vse_poteze = 40
v_desno = 20

# Izračun s formulo za kombinacije

def stevilo_moznih_poti(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))

print(int(stevilo_moznih_poti(vse_poteze, v_desno)))
