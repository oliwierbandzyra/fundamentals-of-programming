###
# Suma liczb z przedziału <x, y> podzielnych przez 2 i 3, a niepodzielnych przez 4
#
def f(x, y):
    total = 0
    for n in range(x, y + 1):
        # % daje resztę z dzielenia; reszta 0 oznacza podzielność
        if n % 2 == 0 and n % 3 == 0 and n % 4 != 0:
            total = total + n
    return total

if __name__ == "__main__":
    print('f(1,20) returns', f(1, 20))
    print('f(10,30) returns', f(10, 30))
