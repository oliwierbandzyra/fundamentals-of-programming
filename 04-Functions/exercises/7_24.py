###
# Oblicza wartość wyrażenia z dodawaniem i odejmowaniem cyfr
#
def f(expression):
    # pierwszy znak to pierwsza liczba
    result = int(expression[0])
    # dalej znaki idą parami: operator, cyfra (np. '+3', '-4')
    # range(1, długość, 2) przeskakuje co 2 znaki, od drugiego znaku
    for i in range(1, len(expression), 2):
        operator = expression[i]
        digit = int(expression[i + 1])
        if operator == '+':
            result = result + digit
        else:
            result = result - digit
    return result

if __name__ == "__main__":
    print('f("2+3") returns', f("2+3"))
    print('f("3+8+1") returns', f("3+8+1"))
    print('f("2+3-4+5-0") returns', f("2+3-4+5-0"))
