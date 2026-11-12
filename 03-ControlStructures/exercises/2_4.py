###
# Simple calculator
#

number1 = int(input('Enter first number: '))
number2 = int(input('Enter second number: '))
operator = input('Enter operator (+, -, *, /): ')
result = 0

# Dobieranie odpowiedniego działania na podstawie wpisanego znaku
if operator == '+':
    result = number1 + number2
elif operator == '-':
    result = number1 - number2
elif operator == '*':
    result = number1 * number2
elif operator == '/':
    result = number1 / number2

print(f'{number1} {operator} {number2} = {result}')