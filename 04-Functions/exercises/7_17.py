###
# Sprawdza, czy wyrażenie jest palindromem
#
def f(palindrome):
    # [::-1] odwraca tekst (czytamy go od końca)
    reversed_text = palindrome[::-1]
    # palindrom to tekst taki sam przed i po odwróceniu
    return palindrome == reversed_text

if __name__ == "__main__":
    print('f("radar") returns', f("radar"))
    print('f("12-11-21") returns', f("12-11-21"))
    print('f("book") returns', f("book"))
