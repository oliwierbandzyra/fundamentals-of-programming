###
# Sprawdza, czy użytkownik ma wszystkie wymagane uprawnienia
#
required_permissions = {"read", "write", "execute"}
user_permissions = {"read", "write"}

# issubset() sprawdza, czy wszystkie elementy jednego zbioru są w drugim.
# Pytamy: czy wszystkie wymagane uprawnienia są wśród uprawnień użytkownika?
has_permissions = required_permissions.issubset(user_permissions)
print(has_permissions)  # False, bo brakuje uprawnienia "execute"
