# Zewnętrzna pętla schodzi co 3 w dół (6, 3, 0), a wewnętrzna dodaje 1, 2, 3 — tworzy układ klawiatury 7-8-9 / 4-5-6 / 1-2-3
i = 6
while i >= 0:
    j = 1
    while j <= 3: 
        print(f'{i+j}', end=' ')
        j += 1
    print()
    i -= 3
