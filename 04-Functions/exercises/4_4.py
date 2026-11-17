###
# Oblicza sumę cyfr w liczbie
#
def sum_digits(number):
    # abs() usuwa minus, żeby liczby ujemne też działały
    number = abs(number)
    # zamieniamy liczbę na tekst, dzięki temu możemy przejść po każdej cyfrze
    text = str(number)
    total = 0
    # pętla bierze po kolei każdy znak (cyfrę) z tekstu
    for digit in text:
        # int() zamienia znak z powrotem na liczbę i dodajemy do sumy
        total = total + int(digit)
    return total

any_number = int(input('Enter integer number: '))
result = sum_digits(any_number)
print('The sum of the digits in the number', any_number, 'is', result)
