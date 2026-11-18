###
# Moduł z funkcjami do operacji na tekście
#

# Zwraca liczbę słów w tekście
def count_words(text):
    # split() dzieli tekst na słowa (po spacjach)
    return len(text.split())

# Zwraca tablicę słów uporządkowaną od najdłuższego do najkrótszego
def words_by_length(text):
    words = text.split()
    # key=len - sortujemy według długości słowa, reverse=True - od największej
    return sorted(words, key=len, reverse=True)

# Zwraca tablicę słów uporządkowaną alfabetycznie
def words_alphabetically(text):
    words = text.split()
    # key=str.lower - przy sortowaniu nie rozróżniamy wielkich i małych liter
    return sorted(words, key=str.lower)
