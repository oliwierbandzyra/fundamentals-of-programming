###
# Tłumacz słów z angielskiego na polski (słownik)
#
translations = {
    'computer': 'komputer',
    'mouse': 'myszka',
    'keyboard': 'klawiatura',
    'printer': 'drukarka'
}

# lower() zamienia litery na małe, żeby "Mouse" też zostało znalezione
word = input('Enter a word in English: ').lower()

# 'in' sprawdza, czy takie słowo jest wśród KLUCZY słownika
if word in translations:
    print('Translation:', translations[word])
else:
    print('Translation is not available.')
