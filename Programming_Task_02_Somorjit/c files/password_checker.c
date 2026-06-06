password = input("Enter Password: ")

has_upper = False
has_digit = False

for char in password:
    if char.isupper():
        has_upper = True
    if char.isdigit():
        has_digit = True

if len(password) >= 8 and has_upper and has_digit:
    print("Strong Password")
elif len(password) >= 8 and (has_upper or has_digit):
    print("Moderate Password")
else:
    print("Weak Password")