###
# Wyświetla kursy euro z pliku euro.json (dane z API Narodowego Banku Polskiego)
#
# Plik euro.json pobieramy z adresu (tabela C - kursy kupna i sprzedaży):
# https://api.nbp.pl/api/exchangerates/rates/c/eur/last/10/?format=json
# i zapisujemy w tym samym folderze co program.
#
import json

with open('euro.json', 'r', encoding='utf-8') as file:
    data = json.load(file) # słownik; klucz "rates" zawiera listę kursów

# Nagłówek tabeli. :<16 oznacza, że tekst zajmuje 16 znaków (wyrównanie do lewej)
print(f"{'Date':<16}{'Buying Rate':<16}{'Selling Rate'}")
print('=' * 44)

# Każdy element listy "rates" to słownik z datą (effectiveDate),
# kursem kupna (bid) i kursem sprzedaży (ask)
for rate in data['rates']:
    # :.4f oznacza liczbę z 4 miejscami po przecinku
    print(f"{rate['effectiveDate']:<16}{rate['bid']:<16.4f}{rate['ask']:.4f}")
