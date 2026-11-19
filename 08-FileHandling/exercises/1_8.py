###
# Wypisuje tekst z pliku pets.txt i liczy słowa w tekście
#
word_count = 0 # tu zliczamy wszystkie słowa

with open('pets.txt', 'r') as file:
    for line in file:
        # wypisujemy linię (end="", bo linia ma już znak nowej linii)
        print(line, end="")
        # split() dzieli linię na słowa i zwraca listę,
        # len() podaje, ile jest w niej elementów, czyli słów
        # liczby słów z kolejnych linii dodajemy do sumy
        word_count += len(line.split())

print()
print('Number of words:', word_count)
