###
# Zapisywanie głosów w głosowaniu (plik voting.json)
#
import json

# Odczyt danych z pliku json.
# Przy pierwszym uruchomieniu pliku jeszcze nie ma, więc try-except
# łapie błąd i zaczynamy od pustego słownika
try:
    with open('voting.json', 'r', encoding='utf-8') as file:
        votes = json.load(file) # json.load zamienia zawartość pliku na słownik
except FileNotFoundError:
    votes = {}

# Głosowanie na osobę
person_name = input('Name of the person you are voting for: ')

if person_name in votes:
    # osoba już jest na liście - dodajemy jeden głos
    votes[person_name] += 1
else:
    # nowa osoba - dopisujemy ją z jednym głosem
    votes[person_name] = 1

# Zapis danych do pliku json (indent=4 robi czytelne wcięcia)
with open('voting.json', 'w', encoding='utf-8') as file:
    json.dump(votes, file, indent=4)

print('Current voting results:')
for name, number in votes.items():
    print(name, ':', number)
