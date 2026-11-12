new_password = input('Enter new password: ')
# len liczy znaki, minimum 12
if len(new_password) < 12:
    print('Password too short (min. 12 chars)')
else:
    print('Password ok!')
