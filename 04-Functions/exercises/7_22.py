###
# Zwraca akronim (pierwsze litery wszystkich słów)
#
def f(name):
    result = ''
    # split() dzieli tekst na słowa
    for word in name.split():
        # word[0] to pierwsza litera słowa
        result = result + word[0]
    return result

if __name__ == "__main__":
    print('f("Internet of Things") returns "' + f("Internet of Things") + '"')
    print('f("For Your Information") returns "' + f("For Your Information") + '"')
    print('f("Python") returns "' + f("Python") + '"')
