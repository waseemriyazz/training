string = input("Enter the input string : ")
answer = 1 
for i in string:
    if i == " ":
        answer =  answer + 1
print(answer)