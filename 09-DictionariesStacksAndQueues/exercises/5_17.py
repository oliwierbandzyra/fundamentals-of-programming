###
# Wypisuje dane miast z pliku cities.json
#
import json

# encoding='utf-8' jest potrzebne, bo w nazwach miast są polskie znaki
with open('cities.json', 'r', encoding='utf-8') as file:
    # plik zawiera tablicę słowników, więc data to lista słowników
    data = json.load(file)

# pierwsza pętla bierze kolejne miasta (słowniki), druga wypisuje ich dane
for city in data:
    for key, value in city.items():
        print(key, ':', value)
    print()
