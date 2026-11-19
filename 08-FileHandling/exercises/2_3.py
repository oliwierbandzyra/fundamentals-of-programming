###
# Robi kopię pliku tekstowego
#

# nazwy plików
original_file = 'healthy_lifestyle.txt'
target_file = 'copy_healthy_lifestyle.txt'

# wczytanie całej zawartości oryginalnego pliku
# encoding='utf-8' - w tekście są znaki specjalne (np. ’), które trzeba poprawnie wczytać i zapisać
with open(original_file, 'r', encoding='utf-8') as file:
    content = file.read()

# zapis tej zawartości do nowego pliku (kopia)
with open(target_file, 'w', encoding='utf-8') as file:
    file.write(content)

print('The file', original_file, 'has been copied to', target_file)
