###
# Liczy parzyste wartości w tablicy (pętla while)
#
arr = [34, 7, 19, 4, 21, 8]

even_count = 0
i = 0 # indeks aktualnego elementu
while i < len(arr):
    # liczba jest parzysta, gdy reszta z dzielenia przez 2 wynosi 0
    if arr[i] % 2 == 0:
        even_count = even_count + 1
    i = i + 1 # bez tego pętla nigdy by się nie skończyła

print('Number of even values:', even_count)
