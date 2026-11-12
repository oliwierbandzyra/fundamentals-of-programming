name = ''

# Pętla pyta o imię tak długo, aż użytkownik wpisze cokolwiek (nie zostawi pustego pola)
while name == '':
    name = input('Enter your name: ')

print(f'Hello {name}')
