###
# A program that checks whether the password length is correct.
#

#wpisanie hasła z klawiatury
password = input('Enter password: ')

# Sprawdzamy czy długość hasła wynosi co najmniej 8 znaków
password_ok = len(password) >= 8
print(f'Password length is valid: {password_ok}')