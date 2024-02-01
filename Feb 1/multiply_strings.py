s1 = input("Enter number 1 (NUMBERS ONLY, with no leading zeroes) : ")
s2 = input("Enter number 2 (NUMBERS ONLY, with no leading zeroes) : ")
num1 , num2 = 0 , 0
for i in range(len(s1)):
    num1 = num1 + int(s1[i])*10
for i in range(len(s2)):
    num2 = num2 + int(s2[i])*10
result = num1 * num2
print(result)

