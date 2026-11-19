###
# Reads the entire contents of a file - suma zaparkowanych samochodów
# (w każdej linii pliku car_park.txt jest liczba samochodów z jednego dnia)
#

# Funkcja czyta całą zawartość pliku i zwraca ją jako jeden tekst
def read_from_file(name):
    with open(name) as file:
        content = file.read()
    return content

# wczytanie całego pliku i podział na linie (lista tekstów)
file_content = read_from_file('car_park.txt')
file_lines = file_content.splitlines()

# obliczenie łącznej liczby zaparkowanych samochodów
total = 0
for line in file_lines:
    # linia jest tekstem, więc int() zamienia ją na liczbę, którą dodajemy do sumy
    total += int(line)

print('Total cars parked:', total)
