###
# Porównuje dwie tablice
#

# Zwraca True, jeśli tablice są takie same, w przeciwnym razie False
def compare(array1, array2):
    # różna liczba elementów - tablice na pewno nie są takie same
    if len(array1) != len(array2):
        return False
    # porównujemy elementy o tych samych indeksach
    for i in range(len(array1)):
        if array1[i] != array2[i]:
            return False
    return True

# Wypisuje obie tablice i wynik porównania
def show_comparison(array1, array2):
    print('Array1:', end=" ")
    for value in array1:
        print(value, end=" ")
    print()
    print('Array2:', end=" ")
    for value in array2:
        print(value, end=" ")
    print()
    if compare(array1, array2):
        print('Comparison: arrays are the same')
    else:
        print('Comparison: arrays are different')
    print()

show_comparison(["water", "book", "sky"], ["water", "book", "sky"])
show_comparison([True, False], [True, False, True])
show_comparison([5, 3, 1], [5, 3, 1])
show_comparison([3, 2, 1], [3, 2])
