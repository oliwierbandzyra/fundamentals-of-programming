# kupon 7x7, liczby w wierszu skacza co 7
for row in range(1, 8):
    for col in range(7):
        print(f"{row + col*7:2}", end=" ")
    print()
