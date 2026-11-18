###
# Wypisuje krotkę w odwrotnej kolejności
#
numbers = (10, 20, 30, 40, 50)

# do tekstów doklejamy kolejne elementy, rozdzielone przecinkami
text = ''
for i in range(len(numbers)):
    if i > 0:
        text = text + ','
    text = text + str(numbers[i])
print('Tuple:', text)

# to samo, ale elementy bierzemy od końca
reverse_text = ''
for i in range(len(numbers) - 1, -1, -1):
    if reverse_text != '':
        reverse_text = reverse_text + ','
    reverse_text = reverse_text + str(numbers[i])
print('Reverse order:', reverse_text)
