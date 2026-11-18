###
# Rysuje wykres funkcji f(x) = x^2 - 3
#
import matplotlib.pyplot as plt

x = []
y = []

# tworzymy wartości x od -100 do 100
for n in range(-100, 101):
    x = x + [n]

# dla każdego x obliczamy y = x^2 - 3
for n in x:
    y = y + [n ** 2 - 3]

# rysowanie wykresu
plt.plot(x, y)
plt.show()
