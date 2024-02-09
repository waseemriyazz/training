def read_file_content(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print("Error: File not found.")
        return ""

# Example Usage:
file_path_input = input("Enter the file path: ")
file_content = read_file_content(file_path_input)
print("File Content:", file_content)