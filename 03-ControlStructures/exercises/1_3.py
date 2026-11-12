###
# Checking whether a car exceeded the speed limit
#

# Zdefiniowanie limitu prędkości
speed_limit = 140

# Wczytanie prędkości pojazdu od użytkownika i zamiana na liczbę całkowitą (int)
car_speed = int(input('Enter car speed (km/h): '))

# Sprawdzenie, czy prędkość pojazdu jest większa od limitu
if car_speed > speed_limit:
    print(f'Your speed is {car_speed}km/h')
    print('Warning: speed limit exceeded!!')