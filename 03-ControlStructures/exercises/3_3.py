# Pobieramy wiek użytkownika jako liczbę całkowitą (int)
age = int(input('Enter your age: '))
# Sprawdzamy, czy wiek jest mniejszy niż 18 LUB (or) większy bądź równy 65
if age < 18 or age >= 65:
    # Jeśli spełniony jest chociaż jeden z tych warunków, przysługuje zniżka
    print('You are eligible for a discount')
# W przeciwnym razie (gdy wiek jest od 18 do 64 lat włącznie)
else:
    # Wyświetlamy brak uprawnień do zniżki
    print('You are not eligible for a discount')
