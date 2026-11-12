# Pobieramy liczbę w systemie dziesiętnym od użytkownika jako liczbę całkowitą
num = int(input("Enter decimal number: "))
# Zapamiętujemy oryginalną liczbę w zmiennej original_num, ponieważ zmienna num będzie modyfikowana w pętli
original_num = num
# Tworzymy pusty napis binary, w którym będziemy budować zapis binarny (dwójkowy) liczby
binary = ""
# Jeśli podana liczba to po prostu 0
if num == 0:
    # Jej zapis binarny to również "0"
    binary = "0"
# W przeciwnym razie (dla liczb większych od 0)
else:
    # Powtarzamy dzielenie przez 2 tak długo, jak liczba num jest większa od 0
    while num > 0:
        # Obliczamy resztę z dzielenia przez 2 (będzie to cyfra 0 lub 1)
        remainder = num % 2
        # Zamieniamy cyfrę reszty na tekst (str) i doklejamy ją Z PRZODU dotychczasowego wyniku binarnego
        binary = str(remainder) + binary
        # Wykonujemy dzielenie całkowite przez 2 (operator // odrzuca część ułamkową)
        num = num // 2 
# Wyświetlamy liczbę dziesiętną oraz jej odpowiednik w systemie dwójkowym
print(f"{original_num}(10) = {binary}(2)")
