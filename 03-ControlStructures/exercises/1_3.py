# Ustalamy maksymalny limit prędkości równy 140 (km/h) i zapisujemy go w zmiennej speed_limit
speed_limit = 140
# Pobieramy od użytkownika prędkość samochodu jako tekst (input), zamieniamy na liczbę całkowitą (int) i zapisujemy w zmiennej car_speed
car_speed = int(input('Enter car speed (km/h): '))
# Sprawdzamy warunkiem (if), czy prędkość samochodu jest większa niż dozwolony limit
if car_speed > speed_limit:
    # Jeśli warunek jest prawdziwy, wyświetlamy komunikat z aktualną prędkością (f-string pozwala wstawić wartość zmiennej w nawiasach {})
    print(f'Your speed is {car_speed}km/h')
    # Wyświetlamy ostrzeżenie o przekroczeniu dozwolonej prędkości
    print('Warning: speed limit exceeded!!')
