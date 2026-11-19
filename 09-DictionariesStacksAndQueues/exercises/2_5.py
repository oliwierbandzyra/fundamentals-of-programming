###
# Łączy dwie listy kontaktów i usuwa duplikaty
#
contacts_A = {"john@example.com", "alice@example.com", "bob@example.com"}
contacts_B = {"bob@example.com", "michael@example.com", "sara@example.com"}

# Suma zbiorów (|): wszystkie elementy z obu zbiorów, bez powtórzeń
# (bob@example.com jest w obu listach, ale pojawi się tylko raz)
merged_contacts = contacts_A | contacts_B
print("Merged contacts:", merged_contacts)
