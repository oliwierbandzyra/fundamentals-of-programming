###
# The program simulates five dice rolls.
#
import random                           #import funkcji do losowania
print("Dice rolling simulator")
for i in range(5):                      #pętla for dla 5 wyników rzutu
    dice_roll = random.randint(1,6)     #zmienia rzut kostką do której jest przypisana funkcja random losująca w zakresie od 1,6
    print(dice_roll, end=" ")           #wypisanie wyników
