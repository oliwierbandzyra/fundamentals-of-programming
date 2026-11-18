###
# Wypisuje popularne gry komputerowe: numerowane i posortowane alfabetycznie
#
computer_games = [
    "Minecraft", "Fortnite", "Cyberpunk 2077", "The Witcher 3",
    "League of Legends", "Valorant", "Grand Theft Auto V",
    "Elden Ring", "Apex Legends", "Call of Duty: Warzone"
]

# sorted() to wbudowana funkcja sortująca - zwraca nową, posortowaną listę
sorted_games = sorted(computer_games)

# pętla while: i to indeks aktualnego elementu
i = 0
while i < len(sorted_games):
    # numer to i + 1, bo indeksy zaczynają się od 0
    print(i + 1, sorted_games[i])
    i = i + 1
