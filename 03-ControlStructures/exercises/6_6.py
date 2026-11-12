hours = int(input('Enter number of hours parked: '))
fee = 0

# Naliczamy opłatę w zależności od przedziału godzin parkowania
if 1 <= hours <= 2:
    fee = 5
elif 3 <= hours <= 6:
    fee = 15
elif hours > 6:
    fee = 20

print(f'Parking fee: {fee} PLN')
