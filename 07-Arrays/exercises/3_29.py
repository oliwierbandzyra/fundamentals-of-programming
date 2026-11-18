###
# Wypisuje tablicę dwuwymiarową 2x4 w wierszach i kolumnach
#
arr = [
    [4, 8, 1, 6],
    [3, 5, 9, 2]
]

for row in arr:
    for value in row:
        print(value, end=" ")
    print()
