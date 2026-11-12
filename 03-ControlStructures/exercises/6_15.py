ean = input("Enter EAN-13 article number: ")
# musi miec 13 znakow i same cyfry
if len(ean) == 13 and ean.isdigit():
    print("Article number is correct")
    # 590 na poczatku oznacza ze z Polski
    if ean.startswith("590"):
        print("Article manufactured in Poland")
