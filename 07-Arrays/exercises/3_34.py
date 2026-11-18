###
# Zamienia miejscami pierwszy i ostatni wiersz tablicy 3x5
#

# Wypisuje tablicę w wierszach i kolumnach
def print_array(arr):
    for row in arr:
        for value in row:
            print(f'{value:3}', end="")
        print()

arr = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
]

print('Before:')
print_array(arr)

# zamiana przez zmienną pomocniczą temp (cały wiersz to jeden element listy)
temp = arr[0]
arr[0] = arr[len(arr) - 1]
arr[len(arr) - 1] = temp

print('After:')
print_array(arr)
