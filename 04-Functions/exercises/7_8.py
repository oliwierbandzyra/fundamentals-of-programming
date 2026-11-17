###
# Minimalna liczba monet (1, 2, 5 zł) potrzebna do zapłaty kwoty
#
def f(amount_to_pay):
    # // to dzielenie całkowite, % to reszta z dzielenia
    # Zaczynamy od największej monety, bo wtedy monet jest najmniej
    coins = amount_to_pay // 5
    rest = amount_to_pay % 5
    # z reszty bierzemy monety dwuzłotowe
    coins = coins + rest // 2
    rest = rest % 2
    # to, co zostało, płacimy monetami jednozłotowymi
    coins = coins + rest
    return coins

if __name__ == "__main__":
    print('f(23) returns', f(23))
    print('f(8) returns', f(8))
    print('f(2) returns', f(2))
    print('f(0) returns', f(0))
