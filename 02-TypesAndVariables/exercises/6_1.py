###
# A program that calculates the number of characters
# of your name, surname and full name
#

name = 'Anna'   
surname = 'May' 

# Sprawdzamy długość imienia i nazwiska za pomocą len() i dodajemy
characters_in_name = len(name)
characters_in_surname = len(surname)
full_name = name + surname

# Wyświetlamy informacje z pomocą f-stringa
print(f'Your name has {characters_in_name} characters')
print(f'Your surname has {characters_in_surname} characters')
print(f'Your full name has {len(full_name)} characters')