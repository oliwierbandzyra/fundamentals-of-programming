###
# Oblicza ocenę końcową z testu na podstawie zdobytych punktów
#
def pts_to_grade(points):
    grade = ''
    # Warunki sprawdzamy od największego progu do najmniejszego,
    # dzięki temu pierwszy spełniony warunek daje właściwą ocenę
    if points >= 18:
        grade = 'Excellent'
    elif points >= 14:
        grade = 'Good'
    elif points >= 10:
        grade = 'Satisfactory'
    else:
        grade = 'Fail'
    return grade

test_result = 15
final_grade = pts_to_grade(test_result)
print('You scored', test_result, 'points on the test. Your final grade is', final_grade)
