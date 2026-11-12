i = 6
# zewnetrzna petla leci 6, 3, 0 a wewnetrzna dodaje 1, 2, 3 (klawiatura 789 / 456 / 123)
while i >= 0:
    j = 1
    while j <= 3: 
        print(f'{i+j}', end=' ')
        j += 1
    print()
    i -= 3
