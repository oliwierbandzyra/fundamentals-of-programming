###
# A program that prints results of three dice rolls and the sum.
#

# Zaimportowanie funkcji do losowania
import random

# Generujemy losowe liczby z zakresu 1-6 dla trzech rzutów z pomocą funkcji dla dowolnej liczby całkowitej random.randint()
dice_roll_1 = random.randint(1, 6)
dice_roll_2 = random.randint(1, 6)
dice_roll_3 = random.randint(1, 6)

#dodanie wyników z 3 rzutów
total = dice_roll_1 + dice_roll_2 + dice_roll_3

# Wypisanie f-stringiem wyników  każdego rzutu  i liczby łącznej otrzymanej
print(f'Rolls: {dice_roll_1}, {dice_roll_2}, {dice_roll_3} | Total: {total}')