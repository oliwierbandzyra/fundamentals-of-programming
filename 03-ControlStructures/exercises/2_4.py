# Pobieramy pierwszą liczbę od użytkownika i zamieniamy ją na liczbę całkowitą (int)
number1 = int(input('Enter first number: '))
# Pobieramy drugą liczbę od użytkownika i zamieniamy ją na liczbę całkowitą (int)
number2 = int(input('Enter second number: '))
# Pobieramy znak działania matematycznego (+, -, * lub /)
operator = input('Enter operator (+, -, *, /): ')
# Tworzymy zmienną result na wynik działania i nadajemy jej wartość początkową 0
result = 0
# Jeśli użytkownik wybrał dodawanie ('+')
if operator == '+':
    # Dodajemy obie liczby i zapisujemy wynik w result
    result = number1 + number2
# W przeciwnym razie, jeśli wybrano odejmowanie ('-')
elif operator == '-':
    # Odejmujemy drugą liczbę od pierwszej
    result = number1 - number2
# W przeciwnym razie, jeśli wybrano mnożenie ('*')
elif operator == '*':
    # Mnożymy obie liczby przez siebie
    result = number1 * number2
# W przeciwnym razie, jeśli wybrano dzielenie ('/')
elif operator == '/':
    # Dzielimy pierwszą liczbę przez drugą
    result = number1 / number2
# Wyświetlamy całe działanie wraz z obliczonym wynikiem
print(f'{number1} {operator} {number2} = {result}')
