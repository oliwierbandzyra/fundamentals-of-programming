###
# Wypisuje elementy tablicy, które występują tylko raz
#
arr = [2, 3, 2, 5, 8, 1, 9, 8]

print('Array:', end=" ")
for value in arr:
    print(value, end=" ")
print()

print('Unique elements:', end=" ")
for value in arr:
    # count() zlicza, ile razy wartość występuje w liście
    # unikalny element występuje dokładnie raz
    if arr.count(value) == 1:
        print(value, end=" ")
print()
