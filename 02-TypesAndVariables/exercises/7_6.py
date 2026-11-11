###
# Vehicle speed validity (between 40 and 140 km/h)
#

# Wprowadzenie prędkości pojazdu z klawiatury jako liczby całkowitej
speed = int(input('Enter vehicle speed: '))

# Sprawdzamy czy prędkość mieszcz się w zakresie od 40 do 140 włącznie
speed_valid = 40 <= speed <= 140
print(f'Speed is valid: {speed_valid}')