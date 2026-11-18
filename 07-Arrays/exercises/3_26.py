###
# Rysuje linię od punktu (1, 3) do punktu (8, 10)
#
import matplotlib.pyplot as plt # biblioteka do rysowania wykresów

xpoints = [1, 8] # współrzędne x obu punktów
ypoints = [3, 10] # współrzędne y obu punktów
plt.plot(xpoints, ypoints) # rysuje linię łączącą punkty
plt.show() # wyświetla okno z wykresem
