# Pobieramy od użytkownika tryb jazdy ('A', 'M' lub 'E') i zapisujemy w zmiennej driving_mode
driving_mode = input('Enter driving mode (A/M/E): ')
# Pobieramy przejechany dystans w kilometrach jako liczbę całkowitą (int)
distance = int(input('Enter distance in km: '))
# Tworzymy zmienną fuel_consumption na zużycie paliwa na 100 km i ustawiamy początkowo na 0
fuel_consumption = 0
# Jeśli wybrano tryb 'A' (Auto)
if driving_mode == 'A':
    # Ustawiamy spalanie na 7 litrów na 100 km
    fuel_consumption = 7 
# W przeciwnym razie, jeśli wybrano tryb 'M' (Manual)
elif driving_mode == 'M':
    # Ustawiamy spalanie na 9 litrów na 100 km
    fuel_consumption = 9
# W przeciwnym razie, jeśli wybrano tryb 'E' (Eco)
elif driving_mode == 'E':
    # Ustawiamy spalanie na 6 litrów na 100 km
    fuel_consumption = 6
# Obliczamy całkowite zużycie paliwa: dzielimy dystans przez 100 i mnożymy przez spalanie na 100 km
total_consumption = (distance / 100) * fuel_consumption
# Wyświetlamy podsumowanie z dystansem, trybem jazdy i całkowitym zużyciem paliwa
print(f'Total fuel consumption over a distance of {distance} km in driving mode {driving_mode} is {total_consumption} liters')
