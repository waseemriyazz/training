def all_substring(str):
    answer = []
    for i in range(0, len(str)):
        sub_string = str[i]
        answer.append(sub_string)
        for j in range(i+1, len(str)):
            sub_string = sub_string + str[j]
            answer.append(sub_string)
        
    return answer
print(all_substring("abc"))
# def all_substring(s):
#     answer = []
#     for i in range(len(s)):
#         sub_string = s[i]
#         answer.append(sub_string)
#         for j in range(i+1, len(s)):
#             sub_string += s[j]
#             answer.append(sub_string)
#     return answer

# print(all_substring("abc"))