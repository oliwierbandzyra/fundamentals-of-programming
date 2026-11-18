###
# Zamienia miejscami pierwszą i ostatnią kolumnę tablicy 3x5
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

# w każdym wierszu zamieniamy pierwszy i ostatni element
for row in arr:
    temp = row[0]
    row[0] = row[len(row) - 1]
    row[len(row) - 1] = temp

print('After:')
print_array(arr)
