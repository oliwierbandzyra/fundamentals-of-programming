###
# Liczy, ile samochodów pochodzi z każdego województwa
# (pierwsza litera tablicy rejestracyjnej wskazuje województwo)
#
import csv

# Słownik: litera -> nazwa województwa (wczytany z pliku province.csv)
provinces = {}
with open('province.csv', 'r', encoding='utf-8', newline='') as file:
    reader = csv.reader(file)
    next(reader) # pomijamy pierwszą linię z nagłówkiem (Letter,Name)
    for row in reader:
        # row[0] to litera, row[1] to nazwa województwa
        provinces[row[0]] = row[1]

# Słownik z licznikami: litera -> liczba samochodów (na początku wszędzie 0)
counts = {}
for letter in provinces:
    counts[letter] = 0

# Odczyt numerów rejestracyjnych z pliku vehicle.txt
with open('vehicle.txt', 'r') as file:
    for line in file:
        plate = line.strip() # strip() usuwa znak nowej linii
        letter = plate[0]    # pierwsza litera numeru
        # zwiększamy licznik tylko dla znanej litery
        if letter in counts:
            counts[letter] += 1

# Wypisanie wyników
for letter, name in provinces.items():
    print(f'{name}: {counts[letter]}')
