###
# Moduł z funkcją maskującą numer karty kredytowej
#
def hide(card_number):
    # card_number[:2]  - pierwsze dwie cyfry
    # card_number[-4:] - ostatnie cztery cyfry
    # w środku zostaje 16 - 2 - 4 = 10 gwiazdek (len() daje długość numeru)
    stars = '*' * (len(card_number) - 6)
    return card_number[:2] + stars + card_number[-4:]
