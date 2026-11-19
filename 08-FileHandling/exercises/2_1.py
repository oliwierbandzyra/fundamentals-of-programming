# Program zapisuje do pliku tekstowego dane o filmie

# Zmienne z danymi filmu
movie_title = "Inception"
director = "Christopher Nolan"
lead_actor = "Leonardo DiCaprio"

# Nazwa pliku, do którego zapisujemy
file_name = 'movie_details.txt'

# 'w' (write) tworzy plik albo nadpisuje go, jeśli już istnieje
with open(file_name, 'w') as file:
    # write() zapisuje jeden tekst do pliku
    # \n oznacza przejście do nowej linii - bez tego wszystko byłoby w jednej linii
    file.write(f"Movie Title: {movie_title}\n")
    file.write(f"Director: {director}\n")
    file.write(f"Lead Actor: {lead_actor}\n")

print(f"Movie details have been written to {file_name}.")
