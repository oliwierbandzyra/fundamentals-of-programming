###
# Wypisuje najdłuższe imię z tablicy
#
names = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]

print('Names:', end=" ")
for name in names:
    print(name, end=" ")
print()

# zakładamy, że najdłuższe jest pierwsze imię
longest = names[0]
for name in names:
    # len() zwraca liczbę znaków w tekście
    if len(name) > len(longest):
        longest = name

print('Longest name:', longest)
