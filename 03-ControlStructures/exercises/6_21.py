amount = int(input("Enter the amount in PLN: "))
print(f"The amount of PLN {amount} in coins:")
# // daje ile monet sie miesci a % ile reszty zostaje do rozmienienia
coins_5 = amount // 5
amount = amount % 5
coins_2 = amount // 2
amount = amount % 2
coins_1 = amount
print(f"5 PLN coins: {coins_5}")
print(f"2 PLN coins: {coins_2}")
print(f"1 PLN coins: {coins_1}")
