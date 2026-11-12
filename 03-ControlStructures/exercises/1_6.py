number = int(input('Enter number: '))

# Operator % (modulo) zwraca resztę z dzielenia — jeśli reszta przez 2 to 0, liczba jest parzysta
if number % 2 == 0:
    print(f'{number} is even')
else:
    print(f'{number} is odd')
