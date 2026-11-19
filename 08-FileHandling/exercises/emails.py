###
# Moduł z funkcjami pobierającymi dane z surowego e-maila (plik email.txt)
#
import re

# Funkcja pomocnicza - wczytuje cały e-mail z pliku
def read_email(file_name='email.txt'):
    with open(file_name, 'r') as file:
        return file.read()

# Zwraca adres e-mail nadawcy (linia zaczynająca się od From:)
def email_sender():
    email = read_email()
    # ^From:  - linia zaczyna się od "From:"
    # .*?     - dowolne znaki (np. imię nadawcy) aż do adresu
    # ([\w.+-]+@[\w-]+(\.[\w-]+)+) - wzorzec adresu e-mail: nazwa@domena.pl
    # re.MULTILINE sprawia, że ^ działa na początku każdej linii
    match = re.search(r'^From:.*?([\w.+-]+@[\w-]+(?:\.[\w-]+)+)', email, re.MULTILINE)
    if match:
        return match.group(1)
    return 'not found'

# Zwraca adres e-mail odbiorcy (linia zaczynająca się od To:)
def email_recipient():
    email = read_email()
    match = re.search(r'^To:.*?([\w.+-]+@[\w-]+(?:\.[\w-]+)+)', email, re.MULTILINE)
    if match:
        return match.group(1)
    return 'not found'

# Zwraca temat e-maila (linia zaczynająca się od Subject:)
def email_subject():
    email = read_email()
    # \s* - spacje po dwukropku, (.*) - cała reszta linii
    match = re.search(r'^Subject:\s*(.*)$', email, re.MULTILINE)
    if match:
        return match.group(1)
    return 'not found'

# Zwraca treść e-maila (wszystko po pierwszej pustej linii)
def email_body():
    email = read_email()
    # \n\n - pusta linia oddziela nagłówek od treści
    # re.DOTALL sprawia, że kropka obejmuje też znaki nowej linii
    match = re.search(r'\n\n(.*)', email, re.DOTALL)
    if match:
        return match.group(1).strip()
    return 'not found'
