###
# Sprawdza poprawność hasła: min. 6 znaków i każdy znak tylko raz
#
def f(password):
    # warunek 1: długość co najmniej 6
    if len(password) < 6:
        return False
    # warunek 2: żaden znak nie może się powtarzać
    for character in password:
        if password.count(character) > 1:
            return False
    return True

if __name__ == "__main__":
    print('f("ax15") returns', f("ax15"))
    print('f("book123") returns', f("book123"))
    print('f("A2water3") returns', f("A2water3"))
    print('f("qwerty") returns', f("qwerty"))
    print('f("") returns', f(""))
