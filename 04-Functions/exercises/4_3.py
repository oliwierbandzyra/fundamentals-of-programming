###
# Oblicza pole trójkąta na podstawie długości jego boków
#
import math

# Definicja funkcji (def) - wzór Herona
def triangle_area(a, b, c):
    # p to połowa obwodu trójkąta
    p = (a + b + c) / 2
    # pole = pierwiastek z p*(p-a)*(p-b)*(p-c)
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    # return zwraca wynik do miejsca, z którego wywołano funkcję
    return area

# Boki wczytane z klawiatury (float, bo mogą być ułamkowe)
side_a = float(input('Enter side a: '))
side_b = float(input('Enter side b: '))
side_c = float(input('Enter side c: '))
print('The area of a triangle with sides', side_a, side_b, side_c, 'is', triangle_area(side_a, side_b, side_c))

# Trzy zadane trójkąty - wywołujemy tę samą funkcję z różnymi danymi
print('The area of a triangle with sides 3, 4, 5 is', triangle_area(3, 4, 5))
print('The area of a triangle with sides 5, 12, 13 is', triangle_area(5, 12, 13))
print('The area of a triangle with sides 7, 24, 25 is', triangle_area(7, 24, 25))
