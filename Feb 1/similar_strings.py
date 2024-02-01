# def similar_strings(s1, s2):
#     if len(s1)%2!=0 or len(s1)%2!=0 or len(s1)!= len(s2):
#         return False
#     left_half_s1=s1[:len(s1)//2]
#     right_half_s1 = s1[len(s1)//2:]
#     left_half_s2=s2[:len(s2)//2]
#     right_half_s1 = s2[len(s2)//2:]
    
# s = "abcd"
# print(s[:len(s)//2])
# print(s[len(s)//2:])



def similarStrings(a, b):

    # Base case
    if len(a) % 2 == 1:
        if a == b:
            return True
        else:
            return False

    # Generate all combinations
    a1 = a[: len(a) // 2]
    a2 = a[len(a) // 2 :]
    b1 = b[: len(b) // 2]
    b2 = b[len(b) // 2 :]

    # If given condition is satisfied then return true else return false
    if (similarStrings(a1, b1) == True and similarStrings(a2, b2) == True) or (
        similarStrings(a2, b1) == True and similarStrings(a1, b2) == True):
        return True
    else:
        return False
    
s1 = input("Enter string 1 : ")
s2 = input("Enter string 1 : ")
if similarStrings(s1, s2):
    print("1")

