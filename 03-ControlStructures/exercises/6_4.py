new_password = input('Enter new password: ')

# len() sprawdza liczbę znaków w haśle — wymagane minimum to 12
if len(new_password) < 12:
    print('Password too short (min. 12 chars)')
else:
    print('Password ok!')
