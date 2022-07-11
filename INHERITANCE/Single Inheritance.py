# Single inheritance in python
#Base class
class Parent_class(object):
#Constructor
 def __init__(self, name, id):
    self.name = name
    self.id = id
    # To fetch employee details
 def Employee_Details(self):
    return self.id , self.name
# To check if this  is a valid employee
 def Employee_check(self):
    if self.id > 500000:
     return " Valid Employee "
    else:
        return " Invalid Employee "
# derived class or the sub class
class Child_class(Parent_class):
    def End(self):
     print( " END OF PROGRAM " )
# Driver code
Employee1 = Parent_class( "Employee1" , 600445)  # parent class object
print( Employee1.Employee_Details() , Employee1.Employee_check() )
Employee2 = Child_class( "Employee2" , 198754) # child class object
print( Employee2.Employee_Details() , Employee2.Employee_check() )
Employee2.End()