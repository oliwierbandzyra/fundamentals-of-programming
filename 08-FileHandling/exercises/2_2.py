###
# Zapisuje do pliku siedem cudów świata w kolejności alfabetycznej
#
seven_wonders = [
    "Great Wall of China",
    "Petra",
    "Christ the Redeemer",
    "Machu Picchu",
    "Chichen Itza",
    "Roman Colosseum",
    "Taj Mahal"
]

# Nazwa pliku, do którego zapisujemy
file_name = 'seven_wonders.txt'

# Sortowanie alfabetyczne (sorted zwraca nową, posortowaną listę)
sorted_wonders = sorted(seven_wonders)

# Zapis danych do pliku
with open(file_name, 'w') as file:
    for item in sorted_wonders:
        # każdy cud w osobnej linii, dlatego dodajemy \n
        file.write(item + '\n')

print('Seven Wonders have been written to', file_name)
