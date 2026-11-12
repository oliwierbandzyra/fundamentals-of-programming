###
# Checking if discount is available
#

age = int(input('Enter your age: '))

# Operator 'or' - rabat dostępny poniżej 18 lub powyżej/równo 65 roku życia
if age < 18 or age >= 65:
    print('You are eligible for a discount')
else:
    print('You are not eligible for a discount')