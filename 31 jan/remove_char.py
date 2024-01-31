s = input("Enter the string : ")
ch = input("Enter the character to be removed : ")
ans  = ""
for i in s:
    if i != ch :
        ans += i 
print(ans) 