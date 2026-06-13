
import numpy as np
import matplotlib.pyplot as plt

# Paramètres
c = 300
a = 5.07

# point d'intersection des deux courbes (pour que la courbe soit continue)
b = 300 - a * 1985

# itervalles des deux morceaux de courbe
x1 = np.linspace(1800, 1985, 100)
x2 = np.linspace(1985, 2050, 100)

# fonctions
y1 = np.full_like(x1, c)
y2 = a * x2 + b

# graph
plt.plot(x1, y1,)
plt.plot(x2, y2,)


plt.xlabel("Année")
plt.ylabel("Concentration CH₄ (ppb)")
plt.title("Évolution du méthane")
plt.legend()
plt.grid()

plt.show()
