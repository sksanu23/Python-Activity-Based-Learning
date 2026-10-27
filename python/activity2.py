
# Case Study 29: Password Policy Validation Engine

password = input("Enter a password: ")

upper = False
lower = False
digit = False
special = False

special_chars = "!@#$%^&*"

for ch in password:
    if ch.isupper():
        upper = True
    elif ch.islower():
        lower = True
    elif ch.isdigit():
        digit = True
    elif ch in special_chars:
        special = True

length_ok = len(password) >= 8
space_ok = " " not in password

print("\n--- PASSWORD VALIDATION ---")
print("Minimum 8 characters:", length_ok)
print("Uppercase letter:", upper)
print("Lowercase letter:", lower)
print("Digit:", digit)
print("Special character:", special)
print("No spaces:", space_ok)

if (length_ok and upper and lower and digit
        and special and space_ok):
    print("Result: VALID PASSWORD")
else:
    print("Result: INVALID PASSWORD")