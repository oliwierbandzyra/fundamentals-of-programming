###
# Oblicza, wypisuje i zapisuje do pliku liczby od 1 do 100
# oraz ich drugie i trzecie potęgi
#

# otwieramy plik do zapisu ('w' - utworzy go albo nadpisze)
with open('powers.txt', 'w') as file:
    # range(1, 101) daje liczby od 1 do 100 włącznie
    for n in range(1, 101):
        # ** to potęgowanie
        line = f'{n},{n ** 2},{n ** 3}'
        print(line)
        # zapis do pliku, \n przenosi do nowej linii
        file.write(line + '\n')
