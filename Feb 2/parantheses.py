# """class takes a string as parameter
# a method which checks if the string is valid or not

# """
# class Paranthesis:
#     def __init__(self, string):
#         self.string = string

#     def isValid(self):
#         s = []
#         for i in self.string:
#             if i == "(" or i == "{" or i == "[":
#                 
#                 s.append(i)
#                 

#             if len(s) == 0:

#                 if i == ")" and s[len(s)-1] == "(":

#                     s.pop()
#                     print("popping")
#                     print(s)

#                 elif i == "}" and s[len(s)-1] == "{":
#                     s.pop()
#                     print("popping")
#                     print(s)

#                 elif i == "]" and s[len(s)-1] == "[":

#                     s.pop()
#                     print("popping")
#                     
#         if(len(s)==0):
#             return True
#         return False
            
        
# s = input("Enter parenthesis")
# myparan=Paranthesis(s)
# print(myparan.isValid())

                


class Paranthesis:
    def __init__(self, string):
        self.string = string

    def isValid(self):
        s = []
        for i in self.string:
            if i == "(" or i == "{" or i == "[":
                s.append(i)
            else:
                if not s:
                    return False 
                
                if (i == ")" and s[-1] != "(") or \
                   (i == "}" and s[-1] != "{") or \
                   (i == "]" and s[-1] != "["):
                    return False  
                s.pop()  
        return not s  


s = input("Enter parentheses: ")
myparan = Paranthesis(s)
print(myparan.isValid())

        
        