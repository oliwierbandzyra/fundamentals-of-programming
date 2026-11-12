# Pobieramy od użytkownika numer miesiąca (od 1 do 12) jako liczbę całkowitą
month = int(input('Enter month number (1..12): '))
# Sprawdzamy od końca roku: jeśli miesiąc jest większy lub równy 10 (czyli 10, 11 lub 12)
if month >= 10:
    # Przypisujemy 4. kwartał
    quarter = 4
# W przeciwnym razie (miesiąc < 10), jeśli jest większy lub równy 7 (czyli 7, 8 lub 9)
elif month >= 7:
    # Przypisujemy 3. kwartał
    quarter = 3
# W przeciwnym razie (miesiąc < 7), jeśli jest większy lub równy 4 (czyli 4, 5 lub 6)
elif month >= 4:
    # Przypisujemy 2. kwartał
    quarter = 2
# W przeciwnym razie (miesiąc < 4), jeśli jest większy lub równy 1 (czyli 1, 2 lub 3)
elif month >= 1:
    # Przypisujemy 1. kwartał
    quarter = 1
# Wyświetlamy informację, w którym kwartale znajduje się podany miesiąc
print(f'Month {month} is in quarter {quarter}')
