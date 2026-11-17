###
# Wypisuje nazwę miesiąca o podanym numerze
#
import months # nasz własny moduł (plik months.py)

def main():
    number = int(input('Enter month number: '))
    print('The name of month', number, 'is', months.month(number))

# Ten blok uruchomi main() tylko gdy plik odpalamy bezpośrednio
if __name__ == "__main__":
    main()
