# 6.Write a Python class Employee with attributes like emp_id, emp_name, emp_salary, and emp_department and methods like calculate_emp_salary, emp_assign_department, and print_employee_details.

# Sample Employee Data:
# "ADAMS", "E7876", 50000, "ACCOUNTING"
# "JONES", "E7499", 45000, "RESEARCH"
# "MARTIN", "E7900", 50000, "SALES"
# "SMITH", "E7698", 55000, "OPERATIONS"
# Use 'assign_department' method to change the department of an employee.
# Use 'print_employee_details' method to print the details of an employee.
# Use 'calculate_emp_salary' method takes two arguments: salary and hours_worked, which is the number of hours worked by the employee. If the number of hours worked is more than 50, the method computes overtime and adds it to the salary. Overtime is calculated as following formula:
# overtime = hours_worked – 50
# Overtime amount = (overtime * (salary / 50))

class Employee:
    def __init__(self, id, name , salary , dept) :
        self.id = id
        self.name = name
        self.salary = salary
        self.dept = dept
    def calculate_emp_salary(self, hours_worked):
        overtime = hours_worked - 50 
        overtime_amount = (overtime * (self.salary/50))
        self.salary = self.salary + overtime_amount

    def emp_assign_department(self, department):
        self.dept= department

    def print_employee_details(self):
        print(f"{self.id} {self.name} {self.salary} {self.dept}")
        

e1 = Employee("ADAMS", "E7876", 50000, "ACCOUNTING")

e2 = Employee("JONES", "E7499", 45000, "RESEARCH")

e3 = Employee("MARTIN", "E7900", 50000, "SALES")

e4 = Employee("SMITH", "E7698", 55000, "OPERATIONS")

e1.print_employee_details()
e1.calculate_emp_salary(60)
e1.print_employee_details()

 
