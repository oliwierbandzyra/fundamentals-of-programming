###
# Losowy element tablicy
#
import random

# Zwraca losowo wybrany element tablicy
def rand_elem(array):
    # losujemy indeks od 0 do ostatniego (obie granice możliwe)
    index = random.randint(0, len(array) - 1)
    return array[index]

colors = ["red", "green", "blue", "yellow", "black"]
print('Array:', colors)
for i in range(5):
    print('Random element:', rand_elem(colors))
