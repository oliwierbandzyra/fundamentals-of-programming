###
# Wykonuje działanie arytmetyczne na dwóch liczbach
#
def f(number1, number2, operator):
    result = 0
    if operator == '+':
        result = number1 + number2
    elif operator == '-':
        result = number1 - number2
    elif operator == '*':
        result = number1 * number2
    elif operator == '%':
        # reszta z dzielenia
        result = number1 % number2
    elif operator == '**':
        # potęgowanie
        result = number1 ** number2
    return result

if __name__ == "__main__":
    print('f(2,3,"+") returns', f(2, 3, "+"))
    print('f(2,3,"%") returns', f(2, 3, "%"))
    print('f(2,3,"**") returns', f(2, 3, "**"))
    print('f(2,3,"*") returns', f(2, 3, "*"))
    print('f(2,3,"-") returns', f(2, 3, "-"))
