current_price = 140.00
previous_price = 200.00
print(f"Current product price: {current_price}")
print(f"Previous product price: {previous_price}")

# Obliczamy procentową obniżkę względem starej ceny
decrease_percentage = ((previous_price - current_price) / previous_price) * 100

if decrease_percentage >= 10:
    print("Buy the product!!")
    print(f"Product price reduced by {int(decrease_percentage)}%")
