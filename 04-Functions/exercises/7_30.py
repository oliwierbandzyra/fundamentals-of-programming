###
# Suma liczb naturalnych od 1 do n - rekurencyjnie
#
def sum_natural(n):
    # przypadek bazowy: suma od 1 do 1 to 1
    if n == 1:
        return 1
    # suma do n to n plus suma do (n-1)
    return n + sum_natural(n - 1)

if __name__ == "__main__":
    print('The sum of natural numbers in the range <1,10> is', sum_natural(10))
