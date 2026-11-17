###
# Sprawdza poprawność kodu produktu (3 cyfry + cyfra kontrolna)
#
def f(product_code):
    # sumujemy pierwsze trzy cyfry
    total = int(product_code[0]) + int(product_code[1]) + int(product_code[2])
    # cyfra kontrolna to reszta z dzielenia sumy przez 7
    control_digit = total % 7
    # kod jest poprawny, gdy czwarta cyfra zgadza się z obliczoną
    return int(product_code[3]) == control_digit

if __name__ == "__main__":
    print('f("1082") returns', f("1082"))
    print('f("2035") returns', f("2035"))
    print('f("1114") returns', f("1114"))
    print('f("7071") returns', f("7071"))
