# Pobieramy pierwszą liczbę całkowitą i zapisujemy w zmiennej x
x = int(input('Enter first number: '))
# Pobieramy drugą liczbę całkowitą i zapisujemy w zmiennej y
y = int(input('Enter second number: '))
# Sprawdzamy, czy x NIE jest ujemny (not x < 0) LUB (or) y NIE jest ujemny (not y < 0)
if not x < 0 or not y < 0:
    # Jeśli przynajmniej jedna z liczb jest >= 0, wyświetlamy odpowiedni komunikat
    print(f'At least one of the numbers {x} and {y} is not negative')
