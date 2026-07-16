#Also known as regexes are like patterns to match inputs from user
import re
email = input("What's your email? ").strip()

if "@" in email and "." in email:
    print("Valid")
else:
    print("Invalid")


username, domain = email.split("@")
if username and domain.endswith(".edu"):
    print("Valid")
else:
    print("Invalid")


if re.search(r"^[^@].+@[^@].+\.edu$", email): #to not interpret the \ (raw-string)
    print("Valid")
else:
    print("Invalid")
   