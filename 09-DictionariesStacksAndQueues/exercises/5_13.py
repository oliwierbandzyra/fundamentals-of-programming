###
# Kalkulator wyrażeń w odwrotnej notacji polskiej (RPN) - stos
# Wpisujemy po jednej wartości: liczbę, operator (+ - * /) albo znak =
#
import queue

stack = queue.LifoQueue()

while True:
    value = input('Enter number, operator or = : ')

    if value == '=':
        # znak = - zdejmujemy ze stosu wynik i kończymy
        print('Result:', stack.get())
        break
    elif value in ['+', '-', '*', '/']:
        # operator - zdejmujemy ze stosu dwie liczby
        # (najpierw drugi argument b, potem pierwszy a)
        b = stack.get()
        a = stack.get()
        if value == '+':
            result = a + b
        elif value == '-':
            result = a - b
        elif value == '*':
            result = a * b
        else:
            result = a / b
        # wynik działania odkładamy z powrotem na stos
        stack.put(result)
    else:
        # w pozostałych przypadkach to liczba - odkładamy ją na stos
        stack.put(float(value))
