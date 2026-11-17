###
# Suma powtarzających się cyfr w liczbie
#
def f(number):
    text = str(abs(number))
    total = 0
    for character in text:
        # count() liczy, ile razy dana cyfra występuje w liczbie
        # jeśli więcej niż raz, to cyfra się powtarza i dodajemy ją do sumy
        if text.count(character) > 1:
            total = total + int(character)
    return total

if __name__ == "__main__":
    print('f(1027) returns', f(1027))
    print('f(230335) returns', f(230335))
    print('f(513553007) returns', f(513553007))
