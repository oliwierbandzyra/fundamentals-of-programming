###
# Sprawdza, czy podana liczba występuje w tablicy
#

# Zwraca True, jeśli liczba jest w tablicy
def occurs(number, array):
    for value in array:
        if value == number:
            # od razu kończymy - znaleźliśmy liczbę
            return True
    # pętla się skończyła i nic nie znaleziono
    return False

arr = [15, 38, 7, 23, 14]
number = int(input('Number: '))

print('Array:', end=" ")
for value in arr:
    print(value, end=" ")
print()

if occurs(number, arr):
    print('Result: number', number, 'appears in the array')
else:
    print('Result: number', number, 'does not appear in the array')
