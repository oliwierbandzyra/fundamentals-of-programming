a, b = 0, 1
# ciag fibonacciego - kolejna liczba to suma dwoch poprzednich
for i in range(20):
    print(a, end=" ")
    a, b = b, a + b
