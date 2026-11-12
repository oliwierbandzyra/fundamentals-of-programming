# Pobieramy od użytkownika kod kreskowy EAN-13 jako tekst
ean = input("Enter EAN-13 article number: ")
# Sprawdzamy, czy kod ma dokładnie 13 znaków (len) ORAZ czy wszystkie znaki są cyframi (isdigit)
if len(ean) == 13 and ean.isdigit():
    # Jeśli oba warunki są spełnione, potwierdzamy poprawność numeru artykułu
    print("Article number is correct")
    # Metoda startswith("590") sprawdza, czy kod zaczyna się od cyfr 590 (prefiks Polski)
    if ean.startswith("590"):
        # Jeśli zaczyna się od 590, informujemy, że produkt wyprodukowano w Polsce
        print("Article manufactured in Poland")
