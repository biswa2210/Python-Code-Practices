class Employee:
    empCount=0
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        Employee.empCount+=1
    def displayCount(self):
        print("THE EMPLOYEE = %d" %Employee.empCount)
    def displayEmployee(self):
        print("Name : ",self.name,", Salary : ",self.salary)
emp1=Employee("BISWA",5000)
emp2=Employee("ROMI",7000)
emp1.displayEmployee()
emp2.displayEmployee()
print("TOTAL EMPLOYEE = %d" %Employee.empCount)
