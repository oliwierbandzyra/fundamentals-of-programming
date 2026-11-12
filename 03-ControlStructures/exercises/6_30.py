# Kupon totolotka 7x7: liczby w wierszu rosną co 7 (kolumny 1-7, 8-14 itd.)
for row in range(1, 8):
    for col in range(7):
        print(f"{row + col*7:2}", end=" ")  # :2 wyrównuje liczby jednocyfrowe spacją
    print()
