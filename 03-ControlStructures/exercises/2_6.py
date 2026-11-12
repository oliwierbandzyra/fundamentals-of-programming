number = int(input('Enter number: '))
# czy dodatnia ujemna czy 0
if number > 0:
    print(f'Number {number} is positive')
elif number < 0:
    print(f'Number {number} is negative')
else:
    print('Number is 0')
