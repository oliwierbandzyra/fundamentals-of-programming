###
# Kopiuje dane książek z pliku books.csv do osobnych plików według gatunku
#
import csv

# gatunki i odpowiadające im nazwy plików (na tych samych pozycjach list)
genres = ['Fantasy', 'Historical', 'Romance', 'Classic']
filenames = ['books_fantasy.txt', 'books_historical.txt',
             'books_romance.txt', 'books_classic.txt']

# Wczytuje cały plik CSV; zwraca nagłówek i listę wierszy
def read_books(file_name):
    with open(file_name, 'r', encoding='utf-8', newline='') as file:
        rows = list(csv.reader(file)) # każdy wiersz to lista wartości
    header = rows[0]
    books = rows[1:]
    return header, books

# Szuka w nagłówku numeru kolumny, której nazwa zawiera dane słowo
def find_column(header, word):
    for i in range(len(header)):
        if word in header[i].lower():
            return i

# Zwraca tylko te książki, które należą do danego gatunku
def select_genre(books, genre_col, genre):
    selected = []
    for book in books:
        if book[genre_col] == genre:
            selected.append(book)
    return selected

# Zapisuje książki do pliku (csv.writer zadba o poprawny zapis przecinków)
def save_books(file_name, books):
    with open(file_name, 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file, lineterminator='\n')
        for book in books:
            writer.writerow(book)

# Główna część programu
header, books = read_books('books.csv')
genre_col = find_column(header, 'genre')

for i in range(len(genres)):
    selected = select_genre(books, genre_col, genres[i])
    save_books(filenames[i], selected)
    print(genres[i], '-->', filenames[i], '(' + str(len(selected)), 'books)')
