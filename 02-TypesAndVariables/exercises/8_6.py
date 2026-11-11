###
# The program calculates the cost of transporting goods
#

#wpisianie z klawiatury dystansu jako liczby całkowitej
distance = int(input('Enter distance in km: '))

#wpisianie z klawiatury ceny paliwa jako liczby zmiennoprzecinkowej
fuel_price = float(input('Enter fuel price per liter: '))

#wpisianie z klawiatury zużycia paliwa jako liczby zmiennoprzecinkowej
fuel_consumption = float(input('Enter fuel consumption per 100 km (liters): '))

# Obliczamy zużycie paliwa oraz całkowity koszt
total_fuel_consumption = (distance / 100) * fuel_consumption
total_cost = total_fuel_consumption * fuel_price

#wypisanie  z f-stringiem całkowitego zużycia paliwa w litrach z zaokrąglenie do dwóch miejsc po przecinku 
print(f'Total fuel consumption: {total_fuel_consumption:.2f} liters')
#wypisanie całkowitego kosztu transportu z zaokrąglenie do dwóch miejsc po przecinku 
print(f'Total transport cost: {total_cost:.2f} PLN')