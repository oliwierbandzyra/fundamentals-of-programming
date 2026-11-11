###
# Tree cutting condition (circumference >= 150 cm)
#

circumference = float(input('Enter tree circumference in cm: '))

# Drzewo można ściąć, gdy obwód wynosi co najmniej 157 cm bo 50 razy PI to obwód
can_be_cut = circumference >= 157
# wypisanie z f-stringiem zmiennej
print(f'Tree can be cut down: {can_be_cut}')