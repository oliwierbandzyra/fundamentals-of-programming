###
# Wypisuje nazwy plików, których rozszerzenie ma dokładnie 4 znaki (np. .html)
#
import re

# \.      - kropka (kropka musi być zapisana z ukośnikiem)
# \w{4}   - dokładnie 4 litery lub cyfry
# $       - koniec nazwy pliku (po tych 4 znakach nic więcej nie może być)
pattern = r'\.\w{4}$'

with open('files.txt', 'r') as file:
    for line in file:
        file_name = line.strip() # strip() usuwa znak nowej linii z końca
        # re.search sprawdza, czy wzorzec pasuje do końca nazwy
        if re.search(pattern, file_name):
            print(file_name)
