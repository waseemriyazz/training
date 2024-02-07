# 2.Write a Python program to ask user input of a string, then ask user input of what letters they want to remove from the string. User can either put in "odd", "even" or a number "n" that is greater than 2. When user input "odd", it will remove the characters which have odd numbers in the sequence of the string. When user input "even", it will remove the characters which have even numbers in the sequence of the string. When user input "n" number, it will remove the characters which have nth numbers in the sequence of the string. Note that we are talking about the sequence of the letters, so the first letter in a string is number 1, the second is number 2, and so on.
def remove_index(string, num):
    answer = ""
    for i in range (0 , len(string)):
        if i % num == 0:
            continue
        answer = answer + string[i]
    return answer

user_input_string = input("Enter a string: ")
user_input_index = input("Enter odd , even or a number: ")
answer = ""

if user_input_index=="odd":
    answer = remove_index(user_input_string, 2)
elif user_input_index=="even":
    answer = remove_index(user_input_string, 3)
else:
    try:
        number = int(user_input_index)
        answer = remove_index(user_input_string, number + 1)
    except ValueError:
        print("incorrect input")
print(answer)



"""
qwertyuio 
012345678 
123456789 
"""