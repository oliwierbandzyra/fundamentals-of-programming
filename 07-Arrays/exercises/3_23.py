###
# Sprawdza, czy pierwsza tablica jest podzbiorem drugiej
#

# Zwraca True, jeśli wszystkie elementy tablicy a są w tablicy b
def is_subset(a, b):
    for value in a:
        if value not in b:
            # znaleźliśmy element, którego nie ma w b
            return False
    return True

first = [2, 5, 8]
second = [1, 2, 3, 5, 8, 9]
print('Array 1:', first)
print('Array 2:', second)
print('Is the first array a subset of the second one?', is_subset(first, second))

first = [2, 5, 7]
print('Array 1:', first)
print('Array 2:', second)
print('Is the first array a subset of the second one?', is_subset(first, second))
