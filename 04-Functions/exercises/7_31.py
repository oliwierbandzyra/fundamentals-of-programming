###
# Potęga x do n - rekurencyjnie
#
def power(x, n):
    # przypadek bazowy: każda liczba do potęgi 0 to 1
    if n == 0:
        return 1
    # x^n = x * x^(n-1)
    return x * power(x, n - 1)

if __name__ == "__main__":
    print('5^3 =', power(5, 3))
