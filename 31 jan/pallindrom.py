
def ispallindrom(str):
    i, j = 0 , len(str)-1
   
    while(i<j):
        if str[i]!=str[j]:
            
            return False
        i = i + 1 
        j = j - 1 
    return True
    
print(ispallindrom("racecar"))
print(ispallindrom("malayalam"))
print(ispallindrom("waseem"))