###
# Reads from file, line by line - lista krajów z numeracją
# (plik countries.txt musi leżeć w tym samym folderze co program)
#

# with open(...) otwiera plik i sam go zamknie po wyjściu z bloku
# 'r' (read) oznacza otwarcie pliku tylko do odczytu
with open('countries.txt', 'r') as file:
    number = 1 # numer aktualnie wypisywanego kraju
    # pętla for czyta plik linia po linii
    for line in file:
        # end="" - linia z pliku ma już na końcu znak nowej linii,
        # więc print nie może dokładać drugiego
        print(f'{number}. {line}', end="")
        number += 1
