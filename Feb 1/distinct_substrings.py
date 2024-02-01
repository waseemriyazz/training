# def distinct_substrings(s):
#     n = len(s)
#     if n > 26:
#         return -1
#     for i in range(len(s)-1):
#        if s[i] == s[i+1]:

def distinctSubstring(s):
    n = len(s)

    # If 'n' is greater than 26, then we can't make distinct substring of 's'.
    if n > 26:
        return -1

    # Creating array 'occ' to store the occurrences of the characters of string.
    occ = [0 for _ in range(26)]

    # Storing the occurrences of the characters.
    for i in range(0, n):
        occ[ord(s[i]) - ord('a')] += 1

    # Creating variable 'unique' to count the number of unique characters in 's'.
    unique = 0

    # Counting unique characters.
    for i in range(0, 26):
        if occ[i] > 0:
            unique += 1

    # Creating variable 'ans' to store the number of characters we have to change.
    ans = n - unique

    # We are returning our answer here.
    return ans