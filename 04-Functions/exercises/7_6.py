###
# Maskuje numer karty kredytowej i wypisuje go
#
import cards # nasz własny moduł (plik cards.py)

def main():
    number = "5290312400019022"
    print('f("' + number + '") returns "' + cards.hide(number) + '"')

if __name__ == "__main__":
    main()
