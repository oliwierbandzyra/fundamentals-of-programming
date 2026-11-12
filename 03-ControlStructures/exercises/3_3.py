age = int(input('Enter your age: '))
# or - wystarczy ze jeden warunek wejdzie (ponizej 18 albo od 65)
if age < 18 or age >= 65:
    print('You are eligible for a discount')
else:
    print('You are not eligible for a discount')
