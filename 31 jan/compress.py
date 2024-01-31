# s = input ("Enter the string : ")
# def compress (s):
#     ans = ""
    
#     for i in range(0, len(s)-1):
#         if s[i] == s[i+1]:
#             j = i
#             count = 1
#             while s[j] == s[i]:
#                 count =  count + 1
#                 j = j + 1
#             ans = ans + s[i] + str(count)
#             i = j -1 
#         else:
#             ans = ans +s[i]
#     return ans

# print(compress(s))
def compress(s):
    ans = ""
    i = 0
    
    while i < len(s):
        count = 1
        j = i + 1
        while j < len(s) and s[j] == s[i]:
            count += 1
            j += 1
        ans += s[i] + str(count)
        i = j
    
    return ans

s = input("Enter the string: ")
print(compress(s))