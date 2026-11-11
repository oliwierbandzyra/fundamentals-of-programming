###
# A program that calculates the distance to the horizon
#
import math #import modułu matematycznego

# Wczytujemy wysokość obserwatora w metrach z klawiatury i konwertujemy na liczbę zmiennoprzecinkową
h = float(input("Enter height in meters: ")) 

# Obliczamy odległość do horyzontu ze wzoru: d = 3.57 * pierwiastek(h)
d = 3.57 * math.sqrt(h)

#wyświetlamy wynik 
print(f"Distance to the horizon: {d} km") # f (f-string) umożliwia wypisanie zmiennej d czyli otrzymanego wyniku