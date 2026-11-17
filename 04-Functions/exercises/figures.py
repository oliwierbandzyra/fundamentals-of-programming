###
# Moduł z funkcjami rysującymi figury za pomocą modułu turtle
#
import turtle

# Jedno "pióro" (żółw) wspólne dla całego modułu. Dzięki temu funkcje
# potrzebują tylko długości boku, a program główny może to samo pióro
# przesuwać (figures.pen)
pen = turtle.Turtle()

# Rysuje kwadrat o boku length
def draw_square(length):
    for i in range(4):
        pen.forward(length)
        pen.right(90)

# Rysuje trójkąt o boku length (równoboczny, czyli też równoramienny)
def draw_triangle(length):
    for i in range(3):
        pen.forward(length)
        pen.right(120)

# Rysuje prostokąt o bokach a i b
def draw_rectangle(length_a, length_b):
    for i in range(2):
        pen.forward(length_a)
        pen.right(90)
        pen.forward(length_b)
        pen.right(90)
