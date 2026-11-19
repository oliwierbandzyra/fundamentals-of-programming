###
# Liczy linie, znaki i słowa w dowolnym pliku tekstowym
#

# nazwę pliku wpisuje użytkownik
file_name = input('File name: ')

# try-except: jeśli pliku nie ma, program się nie zawiesi,
# tylko wypisze komunikat
try:
    with open(file_name, 'r') as file:
        content = file.read()

    # linie - splitlines() dzieli tekst na linie, len() je liczy
    lines = len(content.splitlines())
    # znaki - długość całego tekstu
    characters = len(content)
    # słowa - split() dzieli tekst na słowa, len() je liczy
    words = len(content.split())

    print('Number of lines:', lines)
    print('Number of characters:', characters)
    print('Number of words:', words)
except FileNotFoundError:
    # ten blok wykona się tylko wtedy, gdy plik nie istnieje
    print('The file', file_name, 'does not exist.')
