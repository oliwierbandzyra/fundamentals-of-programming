###
# Zwraca n gwiazdek oddzielonych znakiem /
#
def f(n):
    result = ''
    for i in range(n):
        # przed każdą gwiazdką oprócz pierwszej dodajemy ukośnik
        if i > 0:
            result = result + '/'
        result = result + '*'
    return result

if __name__ == "__main__":
    print('f(4) returns "' + f(4) + '"')
    print('f(1) returns "' + f(1) + '"')
