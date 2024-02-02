class Myclass:
    def __init__(self, para1, para2) :
        self.para1 = para1
        self.para2 = para2
print("The namespace of Myclass is : ")
print(Myclass.__dict__)