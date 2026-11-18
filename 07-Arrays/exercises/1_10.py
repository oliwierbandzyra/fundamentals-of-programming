###
# Wypisuje statystyki testu
#
test_results = [
    False, True, False, True, True,
    True, True, False, True, True,
    False, True, True, True, False
]

# liczba pytań to długość listy
question_number = len(test_results)

# liczymy poprawne odpowiedzi (True)
correct_answers = 0
for answer in test_results:
    if answer == True:
        correct_answers = correct_answers + 1

# błędne odpowiedzi to reszta pytań
incorrect_answers = question_number - correct_answers

# procent poprawnych odpowiedzi (round zaokrągla do 2 miejsc po przecinku)
percentage = round(correct_answers / question_number * 100, 2)

print('TEST STATISTICS')
print('===============')
print('Number of questions:', question_number)
print('Number of correct answers:', correct_answers)
print('Number of incorrect answers:', incorrect_answers)
print('Percentage of correct answers:', percentage, '%')
