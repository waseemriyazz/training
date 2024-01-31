

# myDict ={"a": 12}
# print(myDict)
# print(myDict["a"])
# myDict["c"]= 1
# print(myDict)


s = input("Enter the string : ")
def highest_occuring_char(string):
    myDict = {}
    maxi = 0 
    ans = ""
    for i in string:
         
        if i in myDict:
            myDict[i] = myDict[i] + 1

        else:
            myDict[i] = 1 

    for key , value in myDict.items():
        maxi = max(maxi, value)
        if value == maxi:
            ans = key
        
    
    return ans

print(highest_occuring_char(s))
    