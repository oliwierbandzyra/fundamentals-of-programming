###
# Checks whether at least one number is not negative
#

x = int(input('Enter first number: '))
y = int(input('Enter second number: '))

# 'not' służy do odwrócenia logicznego wyniku mniejszości
if not x < 0 or not y < 0:
    print(f'At least one of the numbers {x} and {y} is not negative')