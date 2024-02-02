class Student :
    def __init__(self) -> None:
        pass

class Marks :
    def __init__(self) -> None:
        pass

stu = Student()
mark = Marks()

print(isinstance(stu, Student))
print(isinstance(mark, Marks))
print(issubclass(Student, object))
print(issubclass(Marks, object))