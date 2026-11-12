driving_mode = input('Enter driving mode (A/M/E): ')
distance = int(input('Enter distance in km: '))
fuel_consumption = 0

# Ustalamy spalanie na 100 km w zależności od wybranego trybu jazdy
if driving_mode == 'A':
    fuel_consumption = 7 
elif driving_mode == 'M':
    fuel_consumption = 9
elif driving_mode == 'E':
    fuel_consumption = 6

# Przeliczamy spalanie na konkretny przejechany dystans
total_consumption = (distance / 100) * fuel_consumption
print(f'Total fuel consumption over a distance of {distance} km in driving mode {driving_mode} is {total_consumption} liters')
