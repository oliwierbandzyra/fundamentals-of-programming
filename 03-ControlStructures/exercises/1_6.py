# Pobieramy od użytkownika dowolną liczbę całkowitą i zapisujemy ją w zmiennej number
number = int(input('Enter number: '))
# Sprawdzamy, czy reszta z dzielenia liczby przez 2 (operator %) jest równa (==) 0
if number % 2 == 0:
    # Jeśli reszta wynosi 0, liczba jest parzysta — wyświetlamy odpowiedni komunikat
    print(f'{number} is even')
# W przeciwnym razie (gdy reszta z dzielenia przez 2 wynosi 1)
else:
    # Liczba jest nieparzysta — wyświetlamy odpowiedni komunikat
    print(f'{number} is odd')
