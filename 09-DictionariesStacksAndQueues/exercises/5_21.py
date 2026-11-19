###
# Zapisuje opis ulubionej książki do pliku favourite.json
#
import json

# Słownik opisujący ulubioną książkę (wartości różnych typów: tekst, liczby, bool, lista)
favourite = {
    "title": "The Hobbit",
    "author": "J.R.R. Tolkien",
    "year": 1937,
    "pages": 310,
    "genre": ["fantasy", "adventure"],
    "read_more_than_once": True
}

# json.dump zapisuje słownik do pliku w formacie json
with open('favourite.json', 'w', encoding='utf-8') as file:
    json.dump(favourite, file, indent=4)

print('Data has been written to favourite.json')
