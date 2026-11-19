###
# Wypisuje nadawcę, odbiorcę, temat i treść e-maila z pliku email.txt
#
import emails # nasz własny moduł (plik emails.py)

print('Sender:', emails.email_sender())
print('Recipient:', emails.email_recipient())
print('Subject:', emails.email_subject())
print('Body:')
print(emails.email_body())
