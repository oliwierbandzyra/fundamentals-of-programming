###
# Rysuje każdą z figur (kwadrat, trójkąt, prostokąt) dwa razy,
# w różnych miejscach
#
import figures # nasz własny moduł (plik figures.py)
import turtle

# Ustawienie okna
window = turtle.Screen()
window.bgcolor("lightgreen")

# Pióro bierzemy z modułu figures
pen = figures.pen
pen.speed(5)

## Rysowanie figur
# penup() - podnosimy pióro, goto() - przesuwamy żółwia, pendown() - opuszczamy pióro
# Kwadrat 1
pen.penup()
pen.goto(-250, 100)
pen.pendown()
figures.draw_square(80)

# Kwadrat 2
pen.penup()
pen.goto(-250, -100)
pen.pendown()
figures.draw_square(50)

# Trójkąt 1
pen.penup()
pen.goto(-80, 100)
pen.pendown()
figures.draw_triangle(80)

# Trójkąt 2
pen.penup()
pen.goto(-80, -100)
pen.pendown()
figures.draw_triangle(50)

# Prostokąt 1
pen.penup()
pen.goto(100, 100)
pen.pendown()
figures.draw_rectangle(120, 60)

# Prostokąt 2
pen.penup()
pen.goto(100, -100)
pen.pendown()
figures.draw_rectangle(70, 40)

# Ukrycie żółwia i zakończenie
pen.hideturtle()
window.mainloop()
