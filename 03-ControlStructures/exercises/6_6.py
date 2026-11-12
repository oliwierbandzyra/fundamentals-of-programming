# Pobieramy od użytkownika liczbę godzin parkowania jako liczbę całkowitą
hours = int(input('Enter number of hours parked: '))
# Ustawiamy początkową opłatę za parking na 0
fee = 0
# Sprawdzamy, czy liczba godzin mieści się w przedziale od 1 do 2 włącznie
if 1 <= hours <= 2:
    # Opłata wynosi 5 PLN
    fee = 5
# W przeciwnym razie sprawdzamy, czy liczba godzin mieści się w przedziale od 3 do 6 włącznie
elif 3 <= hours <= 6:
    # Opłata wynosi 15 PLN
    fee = 15
# W przeciwnym razie, jeśli parkowano dłużej niż 6 godzin
elif hours > 6:
    # Opłata wynosi 20 PLN
    fee = 20
# Wyświetlamy ostateczną opłatę za parking w PLN
print(f'Parking fee: {fee} PLN')
