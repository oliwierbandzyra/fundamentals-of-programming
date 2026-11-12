size = input('Enter size symbol: ')

# Dopasowujemy odpowiedni opis do podanego symbolu rozmiaru
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
