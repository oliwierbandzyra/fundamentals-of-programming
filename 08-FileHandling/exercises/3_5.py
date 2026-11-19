###
# Sprawdza poprawność nazwy użytkownika i hasła
#
import re

# wczytanie nazwy użytkownika i hasła z klawiatury
username = input('Enter username: ')
password = input('Enter password: ')

# wzorce (kryteria):
# ^        - początek tekstu
# [a-z]    - tylko małe litery
# {6,}     - co najmniej 6 znaków
# $        - koniec tekstu (dzięki temu w całym tekście nie może być innych znaków)
username_pattern = '^[a-z]{6,}$'
# [A-Za-z0-9_] - małe i wielkie litery, cyfry oraz podkreślnik
password_pattern = '^[A-Za-z0-9_]{8,}$'

# re.match zwraca dopasowanie, a gdy tekst nie pasuje - None
username_match = re.match(username_pattern, username)
password_match = re.match(password_pattern, password)

# wypisanie wyników
if username_match and password_match:
    print('Username and password are correct.')
else:
    if not username_match:
        print('Incorrect username: at least 6 characters, only lowercase letters.')
    if not password_match:
        print('Incorrect password: at least 8 characters, only letters, digits and underscore.')
