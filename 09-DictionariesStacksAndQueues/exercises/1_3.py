###
# Słownik opisujący mój telefon (6 par klucz-wartość) i wypisanie jego zawartości
#

# Słownik tworzymy w nawiasach { }. Każdy element to para: klucz : wartość
# Klucz jest "etykietą", po której odczytujemy wartość.
mobile = {
    "OS": "Android",
    "brand": "Samsung",
    "model": "Galaxy S23",
    "memory_GB": 128,
    "screen_inches": 6.1,
    "dual_sim": True
}

# items() zwraca naraz klucz i wartość, więc w pętli for mamy dwie zmienne
for key, value in mobile.items():
    print(f"{key} : {value}")
