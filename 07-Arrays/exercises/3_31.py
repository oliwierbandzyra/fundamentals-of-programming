###
# Tworzy tablicę dwuwymiarową wypełnioną zerami
#

# Zwraca tablicę o x wierszach i y kolumnach wypełnioną zerami
def create_2d_arr(x, y):
    arr = []
    for i in range(x):
        row = []
        for j in range(y):
            row.append(0)
        arr.append(row)
    return arr

# tablica 3 wiersze na 5 kolumn
array = create_2d_arr(3, 5)
for row in array:
    for value in row:
        print(value, end=" ")
    print()
