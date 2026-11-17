###
# Suma cyfr parzystych albo nieparzystych w liczbie
#
def f(number, even):
    total = 0
    # zamieniamy liczbę na tekst, żeby przejść po cyfrach
    for character in str(abs(number)):
        digit = int(character)
        if even == True:
            # dodajemy tylko cyfry parzyste
            if digit % 2 == 0:
                total = total + digit
        else:
            # dodajemy tylko cyfry nieparzyste
            if digit % 2 == 1:
                total = total + digit
    return total

if __name__ == "__main__":
    print('f(3124,True) returns', f(3124, True))
    print('f(3124,False) returns', f(3124, False))
    print('f(20576,False) returns', f(20576, False))
    print('f(20576,True) returns', f(20576, True))
    print('f(13115,True) returns', f(13115, True))
