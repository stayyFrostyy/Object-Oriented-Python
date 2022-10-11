
# Example of the most simple class inheritence

# Define class name
class Person(object):

    # Class Constructor
    def __init__(self, name):
        self.name = name

    # Define a couple functions for the Person Class.
    # Gets name of Person
    def getName(self):
        return self.name
    
    # Checks if person is an employee
    def isEmployee(self):
        return False

# Inherited Class AKA Sub Class
# Note parent class is in sub class parameters
class Employee(Person):
    # A Sub class keeps all functions and attributes of Base Class.
    # Constructor, getName etc
    
    # Overwriting function
    def isEmployee(self):
        return True

# Instantiating Objects
per = Person("Tony")
emp = Employee("Mark")

# Accessing Parent attributes
print("{} || Employee: {}".format(per.getName(), per.isEmployee()))
print("{} || Employee: {}".format(emp.getName(), emp.isEmployee()))
