def validate_password(password):
    if len(password) >= 8 and any(c.isupper() for c in password) and any(c.isdigit() for c in password):
        return True
    else:
        return False

# Example Usage:
password_input = input("Enter your password: ")
if validate_password(password_input):
    print("Password is valid.")
else:
    print("Password is invalid.")