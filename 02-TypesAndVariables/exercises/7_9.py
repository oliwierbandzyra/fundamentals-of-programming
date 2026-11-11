###
# Check if rolled dice is 1 or 6
#

#import funkcji random
import random

#wylosowanie liczby od 1 do 6 całkowitej
dice_roll = random.randint(1, 6)

# Zmienna przyjmuje wartość True, jeśli wylosowano 1 lub 6
special_number = (dice_roll == 1 or dice_roll == 6)

# wypisanie co wypadło z f-stringiem i czy wypadła 1 albo 6 true lub false
print(f'Dice rolled: {dice_roll}')
print(f'Special number (1 or 6): {special_number}')