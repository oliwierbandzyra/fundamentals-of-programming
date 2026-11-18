###
# Rysuje wykres y = sin(x) dla kątów 0-360 stopni
#
import math
import matplotlib.pyplot as plt

x = []
y = []

for angle in range(0, 361):
    x = x + [angle]
    # math.sin liczy w radianach, więc stopnie zamieniamy math.radians
    y = y + [math.sin(math.radians(angle))]

plt.plot(x, y)
plt.show()
