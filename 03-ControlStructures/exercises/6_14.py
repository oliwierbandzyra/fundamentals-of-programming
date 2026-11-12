facebook = True
twitter = False
instagram = True
print(f"facebook = {facebook}")
print(f"twitter = {twitter}")
print(f"instagram = {instagram}")
# sprawdza czy ma konta na przynajmniej 2 portalach
if (facebook and twitter) or (facebook and instagram) or (twitter and instagram):
    print("You are a good influencer!")
