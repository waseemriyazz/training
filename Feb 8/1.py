def divide_numbers(numerator, denominator):
    try:
        result = numerator / denominator
        return result
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return None

# Example usage
numerator_input = float(input("Enter numerator: "))
denominator_input = float(input("Enter denominator: "))
result = divide_numbers(numerator_input, denominator_input)
if result is not None:
    print(f"The result of the division is: {result}")