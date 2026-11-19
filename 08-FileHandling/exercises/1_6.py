###
# Reads the entire contents of a file - lista krajów posortowana alfabetycznie
#

# Funkcja czyta całą zawartość pliku i zwraca ją jako jeden tekst
def read_from_file(name):
    with open(name, 'r') as file:
        content = file.read()
    return content

# wczytanie całego pliku
file_content = read_from_file('countries.txt')

# splitlines() dzieli cały tekst na linie i zapisuje je w liście
file_lines = file_content.splitlines()

# sorted() zwraca nową listę posortowaną alfabetycznie
sorted_lines = sorted(file_lines)

# wypisanie posortowanej listy
for line in sorted_lines:
    print(line)
