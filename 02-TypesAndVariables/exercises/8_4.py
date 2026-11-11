###
# A program that prints your height both in cm and in feet and inches.
#

cm = 178

# Przeliczamy centymetry na cale ogółem (1 cal = 2.54 cm)
inches_total = cm / 2.54

# Obliczamy liczbę stóp (1 stopa = 12 cali) używając dzielenia całkowitego
feet = int(inches_total // 12)

# Reszta cali za pomocą operatora modulo (%)
inches = int(inches_total % 12)

#wypisujemy z f-stringiem
print(f'I am {cm}cm tall, i.e. {feet} feet and {inches} inches')