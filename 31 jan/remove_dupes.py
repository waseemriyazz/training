string = input("Enter the string : ")
def remove_dupes(string):
    ans = string[0]
    for i in range(0, len(string)):
        
        if ans[len(ans)-1] != string[i]:
            ans = ans + string[i]
    return ans
print(remove_dupes(string))
