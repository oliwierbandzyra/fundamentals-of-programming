# Zmienna logiczna określająca, czy użytkownik ma konto na Facebooku (True = tak)
facebook = True
# Zmienna logiczna określająca, czy użytkownik ma konto na Twitterze (False = nie)
twitter = False
# Zmienna logiczna określająca, czy użytkownik ma konto na Instagramie (True = tak)
instagram = True
# Wyświetlamy status konta na Facebooku
print(f"facebook = {facebook}")
# Wyświetlamy status konta na Twitterze
print(f"twitter = {twitter}")
# Wyświetlamy status konta na Instagramie
print(f"instagram = {instagram}")
# Sprawdzamy, czy użytkownik ma konta na przynajmniej dwóch platformach (FB i TW, lub FB i IG, lub TW i IG)
if (facebook and twitter) or (facebook and instagram) or (twitter and instagram):
    # Jeśli ma co najmniej dwa konta, wyświetlamy komunikat, że jest dobrym influencerem
    print("You are a good influencer!")
