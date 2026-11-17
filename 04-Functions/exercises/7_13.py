###
# Zwraca liczby od 1 do n połączone w jeden tekst
#
def f(n):
    result = ''
    for i in range(1, n + 1):
        # str() zamienia liczbę na tekst, żeby można ją było dokleić
        result = result + str(i)
    return result

if __name__ == "__main__":
    print('f(11) returns "' + f(11) + '"')
    print('f(4) returns "' + f(4) + '"')
