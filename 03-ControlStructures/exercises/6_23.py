# Pobieramy od użytkownika liczbę, dla której wyświetlimy tabliczkę mnożenia
number = int(input("Enter number: "))
# Pętla for generuje mnożniki i od 1 do 10 włącznie
for i in range(1, 11):
    # Wyświetlamy działanie (liczba x mnożnik) oraz wynik ich mnożenia
    print(f"{number} x {i} = {number * i}")
