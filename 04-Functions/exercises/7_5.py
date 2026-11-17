###
# Sprawdza, czy wpisana liczba należy do przedziału <2, 15>
#
import ranges # nasz własny moduł (plik ranges.py)

def main():
    number = int(input('A number: '))
    if ranges.in_range(number, 2, 15):
        answer = 'yes'
    else:
        answer = 'no'
    print('Number', number, 'in the range <2,15>:', answer)

if __name__ == "__main__":
    main()
