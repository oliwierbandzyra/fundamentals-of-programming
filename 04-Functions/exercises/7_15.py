###
# Sprawdza, czy w pokoju było jednocześnie co najmniej 3 osoby
#
def f(detector):
    # people - ile osób jest teraz w pokoju
    people = 0
    for sign in detector:
        if sign == '+':
            # ktoś wszedł
            people = people + 1
        else:
            # ktoś wyszedł
            people = people - 1
        # po każdej zmianie sprawdzamy, czy jest już 3 osoby
        if people >= 3:
            return True
    return False

if __name__ == "__main__":
    print('f("+-+++-+---") returns', f("+-+++-+---"))
    print('f("+-+-+-+-") returns', f("+-+-+-+-"))
    print('f("+-++-+--") returns', f("+-++-+--"))
    print('f("+-++-++-+---") returns', f("+-++-++-+---"))
