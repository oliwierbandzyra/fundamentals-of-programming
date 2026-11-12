###
# Checking login and password
#

login = 'joe'
password = 'abcd'
entered_login = input('Login: ')
entered_password = input('Password: ')

# Użycie operatora logicznego 'and' - login i hasło muszą być poprawne jednocześnie
if login == entered_login and password == entered_password:
    print('You are logged in')
else:
    print('Incorrect login or password!!')