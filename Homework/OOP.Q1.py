class Employee:
    def __init__(self, emp_name, emp_id, emp_salary, emp_department):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_salary = emp_salary
        self.emp_department = emp_department
    
    def  calculate_emp_salary(self, salary, hours_worked):
        self.salary = self.emp_salary

        if hours_worked >= 50:
            overtime = hours_worked - 50
            Overtimeamount = (overtime * int((salary / 50)))
            self.salary += Overtimeamount

        

    def emp_assign_department(self, department):
        self.emp_department = department
    
    def  print_employee_details(self):
        print(self.emp_id, self.emp_id, self.emp_salary, self.emp_department)
        
        



Employee1 = Employee("ADAMS", "E7876", 50000, "ACCOUNTING")
Employee2 = Employee("JONES", "E7499", 45000, "RESEARCH")
Employee3 = Employee("MARTIN", "E7900", 50000, "SALES")
Employee4 = Employee("SMITH", "E7698", 55000, "OPERATIONS")    


Employee1.emp_assign_department("PERSONNEL")

print(Employee1.emp_department)


Employee1.calculate_emp_salary(50000, 60)

print

