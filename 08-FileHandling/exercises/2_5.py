###
# Tworzy listę zakupów na podstawie nazw produktów wpisywanych z klawiatury
#

# nazwa pliku z listą zakupów
shopping_list = 'shopping_list.txt'

# Dodaje nazwę produktu na końcu listy zakupów
def add_product(file_name, product_name):
    # 'a' (append) dopisuje na końcu pliku i nie kasuje tego, co już w nim jest
    with open(file_name, 'a') as file:
        file.write(product_name + '\n')

# Wczytywanie kolejnych produktów z klawiatury
product = ""
while product != "0":
    product = input('Enter product name (0 stops): ')
    if product == '0':
        # break przerywa pętlę while - kończymy wpisywanie produktów
        break
    else:
        add_product(shopping_list, product)

print('Your shopping list has been saved to', shopping_list)
