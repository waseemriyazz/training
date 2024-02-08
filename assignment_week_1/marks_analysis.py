class Student:
    def __init__(self,name,  physics, chemistry, maths) :
        self.name = name 
        self.physics = physics
        self.chemistry = chemistry
        self.maths = maths
        self.fail = self.isfail()
    
    def __str__(self) :
        return f"{self.name} {self.physics} {self.chemistry} {self.maths}"
        

    def isfail(self):
        if self.physics < 33 or self.chemistry < 33 or self.maths < 33:
            return True
        return False
    
    def total_marks(self):
        total_marks = self.physics + self.chemistry + self.maths
        return total_marks
    
    def average(self):
        total = self.total_marks() / 3
        return total
    

def get_sub(subject):
    try:
        marks= int(input(f"Enter marks in {subject}"))
        return marks
    except:
        print("Enter an integer value")
        return get_sub(subject)
    

def get_min():
    try:
        min_threshold = int(input("Enter the value of minimum threshold : "))
        return min_threshold
    except:
        print("Enter an integer value")
        return get_min()
    

def get_max():
    try: 
        max_threshold = int(input("Enter the value of maximum threshold : "))
        return max_threshold
    except:
        print("Enter an integer value")
        return get_max()
    

student_list = {}



class_strength = int(input("Enter the number of students: "))



for i in range(class_strength):

    name = input("Enter student name : ")

    physics = get_sub("physics")

    chemistry = get_sub("chemistry")

    math = get_sub("maths")

    s = Student(name, physics, chemistry, math)

    student_list[i] = s


        
min_threshold = get_min()
max_threshold = get_max()


above = []

between = []

below = []

attention = []

failed = []

for student in student_list.values():
    
    if student.average() > max_threshold and student.fail == False:
        above.append(student)

    elif student.average() <= max_threshold  and student.average() >= min_threshold and student.fail ==False:
        between.append(student)

    elif student.average() < min_threshold and student.fail == False:
        below.append(student)

    else:
        attention.append(student)
    if student.fail == True:
        failed.append(student)

while 1 > 0:
    print()
    print("Enter 1 to get list of students above max ")
    print("Enter 2 to get list of students between max and min ")
    print("Enter 3 to get list of students below max ")
    print("Enter 4 to get list of students who need special attention ")
    print("Enter 5 to print the list of students who failed ")
    print("Enter 6 to exit ")
    
    try :
        query = int(input("Enter the analysis you want to perform( 1 , 2 , 3 , 4 , 5 , 6 ): "))

        if query == 1 :
            for student in above:
                print(student)
        elif query == 2 :
            for student in between:
                print(student)
        elif query == 3 :
            for student in below:
                print(student)
        elif query == 4 :
            for student in attention:
                print(student)
        elif query == 5 :
            for student in failed:
                print(student)
        else: 
            print("exiting operation . . .")
            break
    except :
        print("Enter an integer value")    

    

    



        
        




    