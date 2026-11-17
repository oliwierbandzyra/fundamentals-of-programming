###
# Moduł z funkcją zliczającą wystąpienia litery w tekście
#
def count_letter(text, letter):
    counter = 0
    # sprawdzamy po kolei każdy znak tekstu
    for character in text:
        if character == letter:
            counter = counter + 1
    return counter
