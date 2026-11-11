###
# String manipulation
#

movie = "The Lord of the Rings: The Return of the King"

# print number of characters
print('Number of characters: ', len(movie)) # funkcja len() aby otrzymać długość znaków

# print title in capital letters
print('Uppercase: ', movie.upper()) # funkcja upper() aby zamienić na duże literki

# print title in small letters
print('Lowercase: ', movie.lower()) # funkcja lower() aby zamienić na małe literki

# print how many times the vowel "e" appears in the title
print('Count of "e": ', movie.count('e')) # ile razy w tekście jest litera e funkcja count()

# print where in the text is the word "Lord"
print('Index of "Lord": ', movie.find('Lord')) # w którym momencie zaczyna się słowo find()

# print where in the text is the word "dragon"
print('Index of "dragon": ', movie.find('dragon')) # w którym momencie zaczyna się słowo find()