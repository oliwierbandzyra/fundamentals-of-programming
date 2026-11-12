# Pobieramy od użytkownika symbol rozmiaru ubrania (jako tekst) i zapisujemy w zmiennej size
size = input('Enter size symbol: ')
# Sprawdzamy, czy wpisany rozmiar to 'S'
if size == 'S':
    # Jeśli tak, wypisujemy opis małego rozmiaru
    print('S: Small size')
# W przeciwnym razie, jeśli (elif) wpisany rozmiar to 'M'
elif size == 'M':
    # Wypisujemy opis średniego rozmiaru
    print('M: Medium size')
# W przeciwnym razie, jeśli wpisany rozmiar to 'L'
elif size == 'L':
    # Wypisujemy opis dużego rozmiaru
    print('L: Large size')
# W przeciwnym razie, jeśli wpisany rozmiar to 'XL'
elif size == 'XL':
    # Wypisujemy opis bardzo dużego rozmiaru
    print('XL: Extra large size')
# W każdym innym przypadku (gdy wpisano inny symbol niż S, M, L, XL)
else:
    # Wyświetlamy komunikat o niepoprawnym symbolu
    print('Incorrect symbol')
