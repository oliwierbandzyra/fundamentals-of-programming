###
# Wypisuje liczby z pierwszej tablicy, których nie ma w drugiej
#
first = [4, 36, 12, 28, 9, 44, 5]
second = [5, 1, 36]

print('Numbers from the first array that are not in the second array:', end=" ")
for number in first:
    # operator "not in" sprawdza, czy elementu nie ma w liście
    if number not in second:
        print(number, end=" ")
print()
