###
# Checking whether the number entered from the keyboard is even or odd
#

number = int(input('Enter number: '))

# Użycie operatora modulo (%). Jeśli reszta z dzielenia przez 2 wynosi 0, liczba jest parzysta
if number % 2 == 0:
    print(f'{number} is even')
else:
    print(f'{number} is odd')