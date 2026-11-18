###
# Liczy, ile razy wartość występuje w krotce
#
numbers = (50, 20, 40, 50, 30, 50)

text = ''
for i in range(len(numbers)):
    if i > 0:
        text = text + ','
    text = text + str(numbers[i])
print('Tuple:', text)

value = int(input('Value: '))

counter = 0
for number in numbers:
    if number == value:
        counter = counter + 1
print('Number of occurrences:', counter)
