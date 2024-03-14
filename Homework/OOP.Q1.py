class Employee:
    def __init__(self, emp_name, emp_id, emp_salary, emp_department):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_salary = emp_salary
        self.emp_department = emp_department
    
    def  calculate_emp_salary(self, salary, hours_worked):
        self.salary = salary
    
        overtime = 0
        if hours_worked >= 50:
            overtime = hours_worked - 50
            self.salary = self.salary + (overtime * (self.salary / 50))
        print(self.salary)

        

    def emp_assign_department(self, department):
        self.emp_department = department
    
    def  print_employee_details(self):
        print("Employee Name: ", self.emp_name)
        print("Employee ID: ",self.emp_id)
        print("Employee Salary: ",self.emp_salary) 
        print("Employee Department: ",self.emp_department)
        
        



Employee1 = Employee("ADAMS", "E7876", 50000, "ACCOUNTING")
Employee2 = Employee("JONES", "E7499", 45000, "RESEARCH")
Employee3 = Employee("MARTIN", "E7900", 50000, "SALES")
Employee4 = Employee("SMITH", "E7698", 55000, "OPERATIONS")    


Employee1.emp_assign_department("PERSONNEL")
Employee4.emp_assign_department("MARKETING")

print(Employee1.emp_department)
print(Employee2.emp_department)
print(Employee3.emp_department)
print(Employee4.emp_department)

Employee1.calculate_emp_salary(56000, 600)
"""
Employee1.print_employee_details()
Employee2.print_employee_details()
Employee3.print_employee_details()
Employee4.print_employee_details()
"""