###
# Zwraca n-ty wyraz ciągu Fibonacciego (0, 1, 1, 2, 3, 5, ...)
#
def f(n):
    # a - aktualny wyraz, b - następny wyraz
    a = 0
    b = 1
    # przesuwamy się w ciągu o n - 1 miejsc
    for i in range(n - 1):
        next_value = a + b
        a = b
        b = next_value
    return a

if __name__ == "__main__":
    print('f(5) returns', f(5))
    print('f(9) returns', f(9))
