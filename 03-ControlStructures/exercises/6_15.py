ean = input("Enter EAN-13 article number: ")

# Kod EAN-13 musi mieć dokładnie 13 znaków i składać się z samych cyfr
if len(ean) == 13 and ean.isdigit():
    print("Article number is correct")
    # Prefiks 590 oznacza produkt z Polski
    if ean.startswith("590"):
        print("Article manufactured in Poland")
