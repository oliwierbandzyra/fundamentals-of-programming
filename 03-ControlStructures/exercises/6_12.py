amount = int(input("Number of products purchased: "))
price = float(input("Product price: "))

# Pierwsze 2 sztuki w pełnej cenie, a każda kolejna powyżej 2 sztuk z 25% rabatem (* 0.75)
if amount > 2:
    total_to_pay = (2 * price) + ((amount - 2) * price * 0.75)
else:
    total_to_pay = amount * price

# :.2f formatuje kwotę do dwóch miejsc po przecinku
print(f"Amount to pay: {total_to_pay:.2f}")
