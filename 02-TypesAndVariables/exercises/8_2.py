###
# Calculation of circle area and circumference 
#

#import modułu math
import math

# Wczytujemy promień koła z klawiatury
r = float(input('Enter radius r: '))

# Obliczamy pole ze wzoru korzystając też z math.pi aby mieć dokładną wartość liczby pi (pi * r^2) i obwód (2 * pi * r)
area = math.pi * (r ** 2)
circumference = 2 * math.pi * r

#wypisanie z f-stringiem promienia
print(f'Radius: {r}')
#wypisanie z f-stringiem pola koła i zaokrąglenie do dwóch miejsc po przecinku z specyfikatorem
print(f'Area: {area:.2f}')
#wypisanie z f-stringiem obwodu koła i zaokrąglenie do dwóch miejsc po przecinku z specyfikatorem
print(f'Circumference: {circumference:.2f}')