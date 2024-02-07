# 1.Write a function that accepts a line of text and a single letter as input (your program should be able to handle all upper and lower cases) and returns the number of times this letter is the second last character of a word. Note your program should be able to handle different cases. And check if the user input is a single letter. Think about how you deal with words ending with punctuation. Example: Input text = "When the sun rises at dawn, the CHICKEN flies into the window." Input letter = "E" Output = "The letter E has appeared 4 times as the second last letter of a word."
user_input_string = input("Enter a string : ")
user_input_letter = input("Enter the letter : ")
count = 0 
flag = 0
# print(user_input_string.split())

words = user_input_string.lower().strip("!.,:;").split()

if len(words)==1:

    print("Input string should be more than 1 word.")
if len(user_input_letter)!=1:
    
    flag = 1
    count = "Enter one letter only."
if flag == 0:

    for word in words:

        if word[len(word)-2]==user_input_letter.lower():
            count += 1

print(count)


