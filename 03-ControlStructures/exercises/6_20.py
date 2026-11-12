num = int(input("Enter decimal number: "))
original_num = num
binary = ""

# Zamiana liczby dziesiętnej na binarną przez kolejne dzielenie przez 2 i zbieranie reszt od końca
if num == 0:
    binary = "0"
else:
    while num > 0:
        remainder = num % 2
        binary = str(remainder) + binary  # dopisujemy resztę z przodu napisu
        num = num // 2  # dzielenie całkowite (bez reszty)

print(f"{original_num}(10) = {binary}(2)")
