
import numpy as np
import matplotlib.pyplot as plt

# Paramètres
c = 300
a = 5.07

# Calcul de b pour raccord parfait
b = 300 - a * 1985

# Intervalles (années réelles)
x1 = np.linspace(1800, 1985, 100)
x2 = np.linspace(1985, 2050, 100)

# Fonctions
y1 = np.full_like(x1, c)
y2 = a * x2 + b

# Tracé
plt.plot(x1, y1,)
plt.plot(x2, y2,)



# Mise en forme
plt.xlabel("Année")
plt.ylabel("Concentration CH₄ (ppb)")
plt.title("Évolution du méthane")
plt.legend()
plt.grid()

plt.show()
