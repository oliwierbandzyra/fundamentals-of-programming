###
# Wypisuje dane komputera z pliku computer.json
#
import json

# Otwarcie pliku json do odczytu
with open('computer.json', 'r', encoding='utf-8') as file:
    # json.load wczytuje dane z pliku do zmiennej (tutaj powstaje słownik)
    data = json.load(file)

# Wypisanie danych: klucz : wartość
for key, value in data.items():
    print(key, ':', value)
