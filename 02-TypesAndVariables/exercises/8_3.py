###
# A program that reads temperature in degrees Celsius
# and converts it to Kelvin and Fahrenheit.
#

#wprowadz z klawiatury temperature
celsius = float(input('Enter temperature in Celsius: '))

# Przeliczamy na kelwiny i fahrenheity
kelvin = celsius + 273.15
fahrenheit = (celsius * 9/5) + 32

#wypisanie z f stringiem poszczególnych wyników
print(f'Celsius: {celsius}°C')
print(f'Kelvin: {kelvin}K')
print(f'Fahrenheit: {fahrenheit}°F')