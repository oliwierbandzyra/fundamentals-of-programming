x = int(input('Enter first number: '))
y = int(input('Enter second number: '))

# 'not x < 0' oznacza, że x nie jest ujemny (czyli jest >= 0); sprawdzamy czy dotyczy to chociaż jednej z liczb
if not x < 0 or not y < 0:
    print(f'At least one of the numbers {x} and {y} is not negative')
