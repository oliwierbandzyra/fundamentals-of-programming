facebook = True
twitter = False
instagram = True
print(f"facebook = {facebook}")
print(f"twitter = {twitter}")
print(f"instagram = {instagram}")

# Sprawdzamy wszystkie kombinacje par, żeby upewnić się, że aktywne są min. 2 konta
if (facebook and twitter) or (facebook and instagram) or (twitter and instagram):
    print("You are a good influencer!")
