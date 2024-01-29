def print_unique_characters(input_str):
    unique_chars = []
    seen_chars = set()

    for char in input_str:
        if input_str.count(char) == 1 and char not in seen_chars:
            unique_chars.append(char)
            seen_chars.add(char)

    print(''.join(unique_chars))

input_str = "abcab"
print_unique_characters(input_str)