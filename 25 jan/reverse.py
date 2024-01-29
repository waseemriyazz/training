
def reverse_string(input_str):
    reverse = ""
    length = len(input_str)
    for i in range(length, 0, -1):
        reverse += input_str[i-1]
    return reverse

input_str = "Hello, World!"
result = reverse_string(input_str)
print(result)