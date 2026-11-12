# Zapisujemy oryginalny tekst do zaszyfrowania w zmiennej plain_text
plain_text = 'The early bird catches the worm'
# Tworzymy pusty ciąg znaków encrypted_text na zaszyfrowaną wiadomość
encrypted_text = ''
# Pętla for przechodzi przez każdy pojedynczy znak w tekście plain_text
for char in plain_text:
    # Funkcja ord(char) zamienia znak na jego kod liczbowy z tablicy ASCII/Unicode
    char_code = ord(char)
    # Zwiększamy kod znaku o 1 (przesuwamy literę o jedno miejsce dalej w alfabecie/tablicy ASCII)
    char_code = char_code + 1
    # Funkcja chr(char_code) zamienia nowy kod liczbowy z powrotem na znak
    new_char = chr(char_code)
    # Doklejamy zaszyfrowany znak na koniec zmiennej encrypted_text (operator += działa jak: encrypted_text = encrypted_text + new_char)
    encrypted_text += new_char
# Wyświetlamy tekst oryginalny
print(f"Oryginał: {plain_text}")
# Wyświetlamy tekst po zaszyfrowaniu
print(f"Zaszyfrowany: {encrypted_text}")
