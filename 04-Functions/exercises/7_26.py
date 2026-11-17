###
# Zwraca tekst ze znakami oddzielonymi myślnikami
#
def f(text):
    result = ''
    for i in range(len(text)):
        # myślnik dajemy przed każdym znakiem oprócz pierwszego
        if i > 0:
            result = result + '-'
        result = result + text[i]
    return result

if __name__ == "__main__":
    print('f("University") returns "' + f("University") + '"')
    print('f("UE") returns "' + f("UE") + '"')
    print('f("x") returns "' + f("x") + '"')
    print('f("") returns "' + f("") + '"')
