class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name

    def add_student_class(self, student_class):
        self.student_class = student_class

    def display_attributes(self):
        print("Attributes and values of the class:")
        for attr, value in self.__dict__.items():
            print("{}: {}".format(attr, value))

    def remove_student_name(self):
        del self.student_name



student = Student(student_id=1, student_name="Waseem Riyaz")


student.add_student_class("Class 1")
student.display_attributes()


student.remove_student_name()
print()
print("After removing student_name attribute:")
student.display_attributes()
