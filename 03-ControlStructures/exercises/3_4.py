x = int(input('Enter first number: '))
y = int(input('Enter second number: '))
# not x < 0 czyli x nie jest ujemny (jest >= 0), wystarczy jedna taka liczba
if not x < 0 or not y < 0:
    print(f'At least one of the numbers {x} and {y} is not negative')
