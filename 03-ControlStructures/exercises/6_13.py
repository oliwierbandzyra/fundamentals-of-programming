# Pobieramy prędkość samochodu od użytkownika jako liczbę całkowitą
car_speed = int(input("Enter car speed: "))
# Ustalamy minimalną dozwoloną prędkość (np. na autostradzie) na 40
speed_limit_min = 40
# Ustalamy maksymalną dozwoloną prędkość na 140
speed_limit_max = 140
# Sprawdzamy, czy prędkość jest mniejsza niż minimum LUB (or) większa niż maksimum
if car_speed < speed_limit_min or car_speed > speed_limit_max:
    # Jeśli prędkość wykracza poza dozwolony zakres, wyświetlamy ostrzeżenie
    print("Warning: invalid car speed!!")
