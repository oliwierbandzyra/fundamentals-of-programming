# A program that reads your first and last name from the keyboard.
# Store this data in two separate variables.
# Then, print your full name i.e. first and last name separated by a single space.

# Pobieramy imię i nazwisko od użytkownika
first_name = input('Enter your first name: ')
last_name = input('Enter your last name: ')

# Łączymy je spacją w jedną zmienną
full_name = first_name + ' ' + last_name

# Wypisujemy sformatowany komunikat używami f-stringa
print(f'Your first name is {first_name} and your last name is {last_name}')
print(f'And your full name is {full_name}')