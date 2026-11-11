###
# A program that calculates the volume
# and surface area of a cuboid with sides a, b, and c.
# Read the dimensions of the cuboid from the keyboard.
#

# Wczytujemy trzy wymiary prostopadłościanu z klawiatury
a = float(input('a='))
b = float(input('b='))
c = float(input('c='))

# Obliczamy objętość i pole całkowite ze wzorów
volume = a * b * c
surface_area = 2 * (a * b + a * c + b * c)

# Drukujemy wyniki za pomocą f-stringa
print(f'Volume: {volume}')
print(f'Surface area: {surface_area}')