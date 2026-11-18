###
# Suma wartości w ostatniej kolumnie tablicy dwuwymiarowej
#
arr = [
    [7, 3, 7, 9, 0],
    [2, 9, 0, 1, 5],
    [3, 8, 6, 4, 7],
    [8, 7, 1, 1, 5]
]

total = 0
for row in arr:
    # ostatni element każdego wiersza to wartość z ostatniej kolumny
    total = total + row[len(row) - 1]

print('Sum of the last column:', total)
