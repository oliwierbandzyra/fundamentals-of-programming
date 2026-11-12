# Zapisujemy aktualną cenę produktu (140.00) w zmiennej current_price
current_price = 140.00
# Zapisujemy poprzednią cenę produktu (200.00) w zmiennej previous_price
previous_price = 200.00
# Wyświetlamy aktualną cenę
print(f"Current product price: {current_price}")
# Wyświetlamy poprzednią cenę
print(f"Previous product price: {previous_price}")
# Obliczamy procentowy spadek ceny: różnicę cen dzielimy przez cenę poprzednią i mnożymy przez 100
decrease_percentage = ((previous_price - current_price) / previous_price) * 100
# Sprawdzamy, czy cena spadła o co najmniej 10%
if decrease_percentage >= 10:
    # Jeśli tak, zachęcamy do zakupu produktu
    print("Buy the product!!")
    # Wyświetlamy wartość procentową obniżki jako liczbę całkowitą
    print(f"Product price reduced by {int(decrease_percentage)}%")
