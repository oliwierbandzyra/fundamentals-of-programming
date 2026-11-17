###
# Liczba ujemnych liczb parzystych w przedziale <x, y>
#
def f(x, y):
    counter = 0
    # range(x, y + 1) daje liczby od x do y włącznie
    for n in range(x, y + 1):
        # liczba ma być ujemna ORAZ parzysta (reszta z dzielenia przez 2 to 0)
        if n < 0 and n % 2 == 0:
            counter = counter + 1
    return counter

if __name__ == "__main__":
    print('f(-7,8) returns', f(-7, 8))
    print('f(-1,11) returns', f(-1, 11))
