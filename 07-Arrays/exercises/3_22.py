###
# Rozdziela liczby parzyste i nieparzyste: najpierw parzyste, potem nieparzyste
#
arr = [7, 9, 2, 4, 5, 6]
print('arr =', arr)

evens = []
odds = []
for number in arr:
    if number % 2 == 0:
        evens.append(number) # append dodaje element na koniec listy
    else:
        odds.append(number)

# + łączy dwie listy w jedną
arr = evens + odds
print('arr =', arr)
