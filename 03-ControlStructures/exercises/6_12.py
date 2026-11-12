# Pobieramy liczbę zakupionych sztuk produktu jako liczbę całkowitą (int)
amount = int(input("Number of products purchased: "))
# Pobieramy cenę pojedynczego produktu jako liczbę zmiennoprzecinkową (float)
price = float(input("Product price: "))
# Sprawdzamy, czy kupiono więcej niż 2 sztuki produktu
if amount > 2:
    # Pierwsze 2 sztuki kosztują pełną cenę (2 * price), a każda kolejna sztuka (amount - 2) ma 25% rabatu (czyli płacimy 0.75 ceny)
    total_to_pay = (2 * price) + ((amount - 2) * price * 0.75)
# W przeciwnym razie (gdy kupiono 1 lub 2 sztuki)
else:
    # Płacimy pełną cenę za wszystkie sztuki (bez rabatu)
    total_to_pay = amount * price
# Wyświetlamy kwotę do zapłaty zaokrągloną do 2 miejsc po przecinku (:.2f)
print(f"Amount to pay: {total_to_pay:.2f}")
