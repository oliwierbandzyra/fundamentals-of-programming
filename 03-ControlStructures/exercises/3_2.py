# Ustalamy poprawny login w zmiennej login
login = 'joe'
# Ustalamy poprawne hasło w zmiennej password
password = 'abcd'
# Pobieramy od użytkownika wpisany login
entered_login = input('Login: ')
# Pobieramy od użytkownika wpisane hasło
entered_password = input('Password: ')
# Sprawdzamy, czy wpisany login zgadza się z poprawnym ORAZ (and) wpisane hasło zgadza się z poprawnym
if login == entered_login and password == entered_password:
    # Jeśli oba warunki są prawdziwe, wyświetlamy komunikat o zalogowaniu
    print('You are logged in')
# W przeciwnym razie (jeśli login lub hasło, albo oba, są błędne)
else:
    # Wyświetlamy komunikat o błędnych danych logowania
    print('Incorrect login or password!!')
