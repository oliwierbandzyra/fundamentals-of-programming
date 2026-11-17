###
# Sprawdza, czy przynajmniej jedna z trzech liczb jest ujemna
#
def f(n1, n2, n3):
    # or oznacza "lub" - wystarczy, że jeden warunek jest prawdziwy
    return n1 < 0 or n2 < 0 or n3 < 0

if __name__ == "__main__":
    print('f(11,6,-4) returns', f(11, 6, -4))
    print('f(5,4,14) returns', f(5, 4, 14))
