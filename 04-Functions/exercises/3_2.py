###
# Losuje i wypisuje liczbę od 1 do 6, jak rzut kostką
#

# import - dołączamy moduł random, który zawiera funkcje do losowania
import random

# randint(1, 6) losuje liczbę całkowitą z przedziału 1..6 (obie granice są możliwe)
dice = random.randint(1, 6)
print('You rolled', dice)
