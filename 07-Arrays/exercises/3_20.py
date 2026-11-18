###
# Test modułu MyArrays
#
import MyArrays # nasz własny moduł (plik MyArrays.py)

numbers = [7, 3, 8, 5, 2]

# liczby oddzielone przecinkami (budowane pętlą)
text = ''
for i in range(len(numbers)):
    if i > 0:
        text = text + ','
    text = text + str(numbers[i])
print('Numbers:', text)

print('Second largest number:', MyArrays.second_largest(numbers))
print('Difference between largest and smallest:', MyArrays.difference(numbers))
print('Median:', MyArrays.median(numbers))

result = MyArrays.smallest_and_largest(numbers)
print('Smallest and largest number:', str(result[0]) + ',' + str(result[1]))
print('Numbers as a string:', MyArrays.to_minus_string(numbers))
