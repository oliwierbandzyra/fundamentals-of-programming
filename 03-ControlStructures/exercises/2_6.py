# Pobieramy od użytkownika dowolną liczbę całkowitą i zapisujemy w zmiennej number
number = int(input('Enter number: '))
# Sprawdzamy, czy liczba jest większa od zera
if number > 0:
    # Jeśli tak, informujemy, że liczba jest dodatnia
    print(f'Number {number} is positive')
# W przeciwnym razie, jeśli liczba jest mniejsza od zera
elif number < 0:
    # Informujemy, że liczba jest ujemna
    print(f'Number {number} is negative')
# W przeciwnym razie (gdy liczba nie jest ani > 0, ani < 0, czyli musi być równa 0)
else:
    # Informujemy, że liczba to 0
    print('Number is 0')
