# Pobieramy kwotę w złotówkach jako liczbę całkowitą
amount = int(input("Enter the amount in PLN: "))
# Wyświetlamy nagłówek informujący o rozmienianiu kwoty na monety
print(f"The amount of PLN {amount} in coins:")
# Dzielimy całkowicie (//) kwotę przez 5, aby obliczyć ile maksymalnie zmieści się monet 5-złotowych
coins_5 = amount // 5
# Operator modulo (%) oblicza resztę z dzielenia przez 5 — to kwota, która została jeszcze do rozmienienia
amount = amount % 5
# Z pozostałej kwoty obliczamy liczbę monet 2-złotowych przez dzielenie całkowite przez 2
coins_2 = amount // 2
# Obliczamy resztę po wydaniu dwuzłotówek (będzie to 0 lub 1)
amount = amount % 2
# Pozostała reszta to dokładnie liczba monet 1-złotowych
coins_1 = amount
# Wyświetlamy liczbę monet 5 PLN
print(f"5 PLN coins: {coins_5}")
# Wyświetlamy liczbę monet 2 PLN
print(f"2 PLN coins: {coins_2}")
# Wyświetlamy liczbę monet 1 PLN
print(f"1 PLN coins: {coins_1}")
