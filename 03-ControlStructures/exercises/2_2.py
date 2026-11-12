###
# A program for checking clothing sizes
#

size = input('Enter size symbol: ')

# Wykorzystanie instrukcji elif (else-if) do sprawdzenia wielu warunków po kolei
if size == 'S':
    print('S: Small size')
elif size == 'M':
    print('M: Medium size')
elif size == 'L':
    print('L: Large size')
elif size == 'XL':
    print('XL: Extra large size')
else:
    print('Incorrect symbol')