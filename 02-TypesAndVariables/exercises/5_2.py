###
# A program to calculate the volume and surface area of a cube.
# 

# Wczytujemy długość boku z klawiatury, a następnie konwertujemy na liczbę całkowitą
cube_side_string = input('Enter cube side: ')
cube_side = int(cube_side_string) 

# Obliczamy objętość ze wzoru (a^3) oraz pole powierzchni ze wzoru (6 * a^2)
cube_volume = cube_side ** 3
cube_surface_area = 6 * (cube_side ** 2)

# Wyświetlamy wynikiz pomocą f stringa
print(f'The volume of a cube with side {cube_side} is {cube_volume}')
print(f'The surface area of a cube with side {cube_side} is {cube_surface_area}')