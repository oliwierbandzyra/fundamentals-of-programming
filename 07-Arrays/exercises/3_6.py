###
# Znajduje największą i najmniejszą liczbę w tablicy (bez funkcji min i max)
#
arr = [-15, 8, -31, 47, -2, 19]

# na początku zakładamy, że pierwszy element jest i największy, i najmniejszy
maximum = arr[0]
minimum = arr[0]

for value in arr:
    # jeśli trafimy na większą wartość, zapamiętujemy ją
    if value > maximum:
        maximum = value
    # jeśli trafimy na mniejszą wartość, zapamiętujemy ją
    if value < minimum:
        minimum = value

print('Maximum number:', maximum)
print('Minimum number:', minimum)
