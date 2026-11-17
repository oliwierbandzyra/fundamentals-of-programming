###
# Liczy, ile razy litera 'e' występuje w podanym tekście
#
import letters # nasz własny moduł (plik letters.py)

def main():
    text = 'You never get a second chance to make a first impression'
    print(text)
    print("The number of letter 'e':", letters.count_letter(text, 'e'))

if __name__ == "__main__":
    main()
