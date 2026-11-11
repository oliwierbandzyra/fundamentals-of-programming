###
# Exemption from paying taxes for people up to 26 years old
#

# wpisanie wieku z klawiatury liczba całkowita
age = int(input('Enter age: '))

# Sprawdzamy warunek wieku (mniej lub równo 26 lat daje True, w przeciwnym razie False)
no_tax = age <= 26

# wypisanie z f-stringiem
print(f'Exemption from paying taxes: {no_tax}')