###
# Liczy elementy większe od wartości wpisanej z klawiatury
#
numbers = [3.5, 7.2, 1.8, 9.4, 5.0, 6.1, 2.7]

value = float(input('Enter a value: '))

counter = 0
for number in numbers:
    if number > value:
        counter = counter + 1

print('Number of elements greater than', value, ':', counter)
