###
# A program that enables a user to challenge a computer.
#

#import modułu random
import random

# Komputer losuje liczbę od 1 do 6
computer = random.randint(1, 6)

# Użytkownik wpisuje swoją propozycję
you = int(input('Guess dice number (1-6): '))

# Sprawdzamy czy użytkownik zgadł
won = (computer == you)

#wypisanie z użyciem f-stringa co wylosował komputer i czy udało się zgadnąć
print(f'Computer rolled: {computer}')
print(f'You won: {won}')