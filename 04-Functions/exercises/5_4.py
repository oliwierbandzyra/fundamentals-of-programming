###
# Rysuje kwadrat za pomocą funkcji draw_square z modułu figures
#
import figures # nasz własny moduł (plik figures.py)
import turtle

# Ustawienie okna
window = turtle.Screen()
window.bgcolor("lightgreen")

# Pióro bierzemy z modułu figures
pen = figures.pen
pen.speed(5)

# Długość boku
side_length = 100

# Rysujemy kwadrat - cała pętla jest teraz w funkcji
figures.draw_square(side_length)

# Ukrycie żółwia i zakończenie
pen.hideturtle()
window.mainloop()
