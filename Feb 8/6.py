class AssertionErrorNegativeNumber(Exception):
    pass

def process_positive_number(num):
    try:
        assert num >= 0, "Number must be non-negative."
        print("Processing the positive number:", num)
    except AssertionError as e:
        print("Assertion Error:", e)

# Example Usage:
number_input = float(input("Enter a number: "))
process_positive_number(number_input)