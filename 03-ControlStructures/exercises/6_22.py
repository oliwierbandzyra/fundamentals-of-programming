for i in range(1, 31):
    # najpierw warunek na 3 i 5 naraz zeby nie wpadlo w same 3 albo 5
    if i % 3 == 0 and i % 5 == 0:
        print("BINGO", end=" ")
    elif i % 3 == 0:
        print("THREE", end=" ")
    elif i % 5 == 0:
        print("FIVE", end=" ")
    else:
        print(i, end=" ")
