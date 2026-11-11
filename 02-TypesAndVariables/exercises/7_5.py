###
# Vehicle registration numbers in Krakow start with KR or KK
#

#wpisanie numeru rejstracyjnego pojazdu z klawiatury
car_number = input('Enter car registration number: ')

# Sprawdzamy czy pierwsze dwa znaki to "KR" lub "KK" z użyciem or == sprawdza czy wartość jest dokładnie taka sama
is_krakow = car_number[0:2] == "KR" or car_number[0:2] == "KK"
# Wypisanie czy jest z krakowa pojazd
print(f'Car is from Krakow: {is_krakow}')