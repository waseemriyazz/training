class InvalidInputError(Exception):
    pass

def validate_positive_integer(user_input):
    try:
        num = int(user_input)
        if num <= 0:
            raise InvalidInputError("Input must be a positive integer.")
        return num
    except ValueError:
        raise InvalidInputError("Invalid input. Please enter an integer.")

# Example Usage:
user_input = input("Enter a positive integer: ")
try:
    valid_input = validate_positive_integer(user_input)
    print("Valid Input:", valid_input)
except InvalidInputError as e:
    print("Error:", e)