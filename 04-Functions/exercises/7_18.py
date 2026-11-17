###
# Zwraca zdanie bez spacji
#
def f(sentence):
    # replace zamienia każdą spację na pusty tekst, czyli ją usuwa
    return sentence.replace(' ', '')

if __name__ == "__main__":
    print('f("integrated development environment") returns')
    print(f("integrated development environment"))
    print('f("A programming language is a system of notation for writing computer programs") returns')
    print(f("A programming language is a system of notation for writing computer programs"))
