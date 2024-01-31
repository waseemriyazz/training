def are_permutations(s1, s2):
    if "".join(sorted(s1)) == "".join(sorted(s2)):
        return True
    return False
s1 = input("Enter the first string : " )
s2 = input("Enter the second string : ")
print(are_permutations(s1, s2))

