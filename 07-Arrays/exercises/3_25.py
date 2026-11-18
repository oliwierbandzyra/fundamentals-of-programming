###
# Test modułu MyText
#
import MyText # nasz własny moduł (plik MyText.py)

text = "An apple a day keeps the doctor away"

# Zamienia tablicę słów na tekst oddzielony przecinkami
def with_commas(words):
    result = ''
    for i in range(len(words)):
        if i > 0:
            result = result + ','
        result = result + words[i]
    return result

print('Text:', text)
print('Number of words:', MyText.count_words(text))
print('Words from the longest:', with_commas(MyText.words_by_length(text)))
print('Words ordered alphabetically:', with_commas(MyText.words_alphabetically(text)))
