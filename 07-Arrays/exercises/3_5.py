###
# Oblicza drugą potęgę każdego elementu tablicy
#
arr = [8, 2, 5, 1, 9]

print('Array:', end=" ")
for value in arr:
    print(value, end=" ")
print()

print('2nd power:', end=" ")
for value in arr:
    # ** to potęgowanie
    print(value ** 2, end=" ")
print()
