# Pobieramy numer miesiąca (1..12) jako liczbę całkowitą
month = int(input('Enter month number (1..12): '))
# Pobieramy numer dnia miesiąca jako liczbę całkowitą
day = int(input('Enter the day number of the month: '))
# Tworzymy zmienną logiczną day_ok, zakładając na start, że dzień jest niepoprawny (False)
day_ok = False
# Jeśli miesiąc znajduje się na liście miesięcy 31-dniowych
if month in [1, 3, 5, 7, 8, 10, 12]:
    # Sprawdzamy, czy podany dzień mieści się w przedziale od 1 do 31
    if day >= 1 and day <= 31:
        # Jeśli tak, oznaczamy dzień jako poprawny (True)
        day_ok = True
# W przeciwnym razie, jeśli miesiąc znajduje się na liście miesięcy 30-dniowych
elif month in [4, 6, 9, 11]:
    # Sprawdzamy, czy dzień mieści się w przedziale od 1 do 30
    if day >= 1 and day <= 30:
        # Jeśli tak, oznaczamy dzień jako poprawny (True)
        day_ok = True
# W przeciwnym razie, jeśli miesiąc to luty (2)
elif month == 2:
    # Sprawdzamy, czy dzień mieści się w przedziale od 1 do 28
    if day >= 1 and day <= 28:
        # Jeśli tak, oznaczamy dzień jako poprawny (True)
        day_ok = True
# Tworzymy początek komunikatu tekstowego z numerem dnia i miesiąca
message = f'Day {day} for the month {month}'
# Jeśli zmienna day_ok ma wartość True
if day_ok:
    # Wyświetlamy informację, że data jest poprawna
    print(f'{message} is correct')
# W przeciwnym razie (gdy day_ok to False)
else:
    # Wyświetlamy informację, że data jest niepoprawna
    print(f'{message} is incorrect')
