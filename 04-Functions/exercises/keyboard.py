###
# Funkcje do wczytywania z klawiatury różnych typów danych
#
def input_string(message):
    # input() zawsze zwraca tekst
    text = input(message)
    return text

def input_integer(message):
    text = input(message)
    # int() zamienia tekst na liczbę całkowitą
    return int(text)

def input_real(message):
    text = input(message)
    # float() zamienia tekst na liczbę rzeczywistą
    return float(text)

def input_boolean(message):
    text = input(message)
    # jeśli wpisano y (lub Y) zwracamy True, w przeciwnym razie False
    return text.lower() == 'y'
