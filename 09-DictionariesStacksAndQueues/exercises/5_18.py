###
# Wypisuje informacje o psach młodszych niż 5 lat (plik dogs.json)
#
import json

with open('dogs.json', 'r', encoding='utf-8') as file:
    dogs = json.load(file) # lista słowników, każdy słownik to jeden pies

for dog in dogs:
    # dog['age'] to wiek psa
    if dog['age'] < 5:
        for key, value in dog.items():
            print(key, ':', value)
        print()
