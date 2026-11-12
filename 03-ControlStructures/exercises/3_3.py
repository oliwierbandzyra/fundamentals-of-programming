age = int(input('Enter your age: '))

# Operator 'or' oznacza, że wystarczy spełnić jeden z warunków (poniżej 18 lat lub od 65 wzwyż)
if age < 18 or age >= 65:
    print('You are eligible for a discount')
else:
    print('You are not eligible for a discount')
