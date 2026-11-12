plain_text = 'The early bird catches the worm'
encrypted_text = ''

# Szyfr Cezara z przesunięciem o 1: zamieniamy znak na kod ASCII (ord), dodajemy 1 i wracamy na znak (chr)
for char in plain_text:
    char_code = ord(char)
    char_code = char_code + 1
    new_char = chr(char_code)
    encrypted_text += new_char

print(f"Oryginał: {plain_text}")
print(f"Zaszyfrowany: {encrypted_text}")
