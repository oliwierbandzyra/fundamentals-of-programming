amount = int(input("Number of products purchased: "))
price = float(input("Product price: "))
if amount > 2:
    total_to_pay = (2 * price) + ((amount - 2) * price * 0.75)
else:
    total_to_pay = amount * price
print(f"Amount to pay: {total_to_pay:.2f}")