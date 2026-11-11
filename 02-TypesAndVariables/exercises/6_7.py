###
# A program that prints a numerical representation of each letter of your name.
#

name = 'John'

# Pobieramy korzystając z f-string kolejne litery po indeksach i sprawdzamy ich kody ASCII z ord()
print(f'The letter {name[0]} has a code {ord(name[0])}')
print(f'The letter {name[1]} has a code {ord(name[1])}')
print(f'The letter {name[2]} has a code {ord(name[2])}')
print(f'The letter {name[3]} has a code {ord(name[3])}')