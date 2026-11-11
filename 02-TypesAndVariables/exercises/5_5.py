###
# A program that calculates discount and final price
#

# Wczytujemy cenę początkową z klawiatury oraz procent rabatu z klawiatury
price = float(input('Enter price: '))
discount_percent = float(input('Enter discount %: '))

# Obliczamy kwotę obniżki oraz cenę końcową
discount_amount = price * (discount_percent / 100)
final_price = price - discount_amount

# Wyświetlamy z pomocą f-stringa zaokrąglone wyniki do 2 miejsc po przecinku korzystając z formatowania
print(f'Price with discount: {final_price:.2f}')
print(f'Reduction: {discount_amount:.2f}')