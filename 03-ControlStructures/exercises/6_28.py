# Ciąg Fibonacciego: w każdym kroku nowa wartość to suma dwóch poprzednich
a, b = 0, 1
for i in range(20):
    print(a, end=" ")
    a, b = b, a + b
