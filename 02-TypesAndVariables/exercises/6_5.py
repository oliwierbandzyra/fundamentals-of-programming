###
# A program that formats a 9-digit phone number
#

phone = input('Enter phone number: ')

# Dzielimy numer na trzyczęściowe bloki za pomocą wycinków i łączymy myślnikami
formatted_phone = f"{phone[0:3]}-{phone[3:6]}-{phone[6:9]}"
print(f"Phone number: {formatted_phone}")