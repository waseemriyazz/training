# # 3.Write a Python program to create a Caesar encryption. Your program will first ask for the input of a secret message, then ask how many places you wish to shift each letter in the alphabet. In the end, your program will produce the shifted secret message as a string. Your program should be able to handle all upper and lower cases, and check if the user inputs are valid. Note: In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's code or Caesar shift, is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. For example, with a shift of 3, A would be replaced by D, B would become E, and so on. The method is named after Julius Caesar, who used it in his private correspondence. Example: Secret message = "This is a secret message" Shift = 5 Each letter is shifted 5 places down in alphabetical order. Secret output: "ymnx nx f xjhwjy rjxxflj"
#  Hint: 1, the 26 letters in the alphabet are not indexed, put them into a list and index them first. 2, Think about what to do when the shifted letter goes beyond 26. e.g. letter z shifted by 5?
def caesar_cipher(message, shift):
    encrypted_message = ""
    for char in message:
        if char.isalpha():  # Check if the character is an alphabet
            # Determine the base value (uppercase or lowercase)
            base = ord('A') if char.isupper() else ord('a')
            # Apply the shift and wrap around if necessary
            shifted = (ord(char) - base + shift) % 26 + base
            encrypted_message += chr(shifted)
        else:
            encrypted_message += char  # Keep non-alphabetic characters unchanged
    return encrypted_message
# Input from the user
secret_message = input("Enter the secret message: ")
while True:
    try:
        shift = int(input("Enter the number of places to shift each letter (positive integer): "))
        if shift >= 0:
            break
        else:
            print("Please enter a positive integer.")
    except ValueError:
        print("Please enter a valid integer.")

# Encrypt the message
encrypted_message = caesar_cipher(secret_message, shift)

# Output the encrypted message
print("Encrypted message:", encrypted_message)
"""
a 
97
waseem riyaz
shift = 2
w
w + 2
124

"""

