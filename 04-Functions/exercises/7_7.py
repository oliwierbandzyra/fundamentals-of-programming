###
# Sprawdza, czy tekst jest poprawną liczbą binarną
#
def f(binary_number):
    # pusty tekst nie jest liczbą binarną
    if binary_number == '':
        return False
    # jeśli trafimy na znak inny niż 0 lub 1, od razu zwracamy False
    for digit in binary_number:
        if digit != '0' and digit != '1':
            return False
    # jeśli pętla się skończyła, wszystkie znaki były poprawne
    return True

if __name__ == "__main__":
    print('f("101101") returns', f("101101"))
    print('f("1311a10100") returns', f("1311a10100"))
