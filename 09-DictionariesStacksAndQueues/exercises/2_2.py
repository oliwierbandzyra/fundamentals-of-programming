###
# Usuwa zduplikowane adresy e-mail
#
emails = ["john@example.com", "jane@example.com", "john@example.com", "alex@example.com"]

# set() zamienia listę na zbiór. Zbiór nie przechowuje powtórzeń,
# więc duplikaty znikają automatycznie
unique_emails = set(emails)
print(unique_emails)
