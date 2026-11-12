# Pobieramy od użytkownika nowe hasło i zapisujemy je w zmiennej new_password
new_password = input('Enter new password: ')
# Funkcja len() liczy długość tekstu; sprawdzamy, czy hasło ma mniej niż 12 znaków
if len(new_password) < 12:
    # Jeśli ma mniej niż 12 znaków, wyświetlamy komunikat, że jest za krótkie
    print('Password too short (min. 12 chars)')
# W przeciwnym razie (gdy hasło ma 12 lub więcej znaków)
else:
    # Wyświetlamy komunikat, że hasło jest poprawne
    print('Password ok!')
