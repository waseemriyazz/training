class Myclass:
    def __init__(self, para1, para2) :
        self.para1 = para1
        self.para2 = para2
my_object = Myclass(1, "2")
print("The namespace of my instance is : ")
print(my_object.__dict__)