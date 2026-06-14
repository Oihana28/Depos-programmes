import numpy as np
import matplotlib.pyplot as plt

# constantes
a = -5.26
b = 736
c = 380

# point d'intersection plateau / droite (y = 380)
x_inter1 = (b - c) / (-a)   # résolution : -5.26x + 736 = 380

# point où la droite coupe y = 0
x_inter2 = -b / a

# axes
x1 = np.linspace(0, x_inter1, 50)
x2 = np.linspace(x_inter1, x_inter2, 50)
x3 = np.linspace(x_inter2, 300, 50)

# fonctions
y1 = np.full_like(x1, c)        # plateau
y2 = a * x2 + b                # droite
y3 = np.zeros_like(x3)         # nul

# tracé
plt.plot(x1, y1)
plt.plot(x2, y2)
plt.plot(x3, y3)



# mise en forme
plt.xlabel("Altitude (km)")
plt.ylabel("CO2 (ppm)")
plt.title("Proportion du CO2 en fonction de l'altitude")
plt.legend()
plt.grid()

plt.show()
