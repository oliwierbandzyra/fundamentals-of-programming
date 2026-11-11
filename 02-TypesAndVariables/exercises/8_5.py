###
# A program that reads a SWIFT code and prints bank and country code.
#

#wpisanie swift z klawiatury
swift = input('Enter SWIFT code: ')

# Pierwsze 4 znaki to kod banku, kolejne 2 to kod kraju np PKOPPL
bank_code = swift[0:4]
country_code = swift[4:6]

#wypisanie z f-stringiem kodu banku i kodu kraju
print(f'Bank Code: {bank_code}')
print(f'Country Code: {country_code}')