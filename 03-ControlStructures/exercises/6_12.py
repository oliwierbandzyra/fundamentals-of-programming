amount = int(input("Number of products purchased: "))
price = float(input("Product price: "))
# pierwsze 2 sztuki po normalnej cenie, kazda nastepna z rabatem 25% (* 0.75)
if amount > 2:
    total_to_pay = (2 * price) + ((amount - 2) * price * 0.75)
else:
    total_to_pay = amount * price
print(f"Amount to pay: {total_to_pay:.2f}")
