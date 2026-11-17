###
# Zwraca liczbę oczek, która wypadła najwięcej razy z rzędu
#
def f(dice):
    best_digit = dice[0]   # liczba oczek z najdłuższej serii
    best_length = 1        # długość najdłuższej serii
    current_length = 1     # długość aktualnej serii
    # porównujemy każdy rzut z poprzednim
    for i in range(1, len(dice)):
        if dice[i] == dice[i - 1]:
            # ta sama liczba co poprzednio - seria rośnie
            current_length = current_length + 1
        else:
            # inna liczba - zaczynamy nową serię
            current_length = 1
        # jeśli aktualna seria jest rekordowa, zapamiętujemy ją
        if current_length > best_length:
            best_length = current_length
            best_digit = dice[i]
    return int(best_digit)

if __name__ == "__main__":
    print('f("5233165554211") returns', f("5233165554211"))
    print('f("2133") returns', f("2133"))
