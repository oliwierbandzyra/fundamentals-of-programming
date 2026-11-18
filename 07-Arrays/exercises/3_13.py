###
# Sortowanie bąbelkowe
#

# Zwraca posortowaną tablicę (rosnąco)
def bubblesort(array):
    n = len(array)
    for i in range(n):
        for j in range(n - i - 1):
            # zamiana sąsiadów, jeśli są w złej kolejności
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
    return array

# Trzy przykładowe tablice
# Uwaga: funkcja zmienia oryginalną listę, dlatego "Before" wypisujemy PRZED sortowaniem
arr1 = [5, 2, 9, 1, 7]
print('Before:', arr1)
print('After: ', bubblesort(arr1))

arr2 = [10, -3, 8, 0, -7, 4]
print('Before:', arr2)
print('After: ', bubblesort(arr2))

arr3 = [3, 3, 1, 2]
print('Before:', arr3)
print('After: ', bubblesort(arr3))
