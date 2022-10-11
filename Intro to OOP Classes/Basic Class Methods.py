
# Introduction to Class Methods

# Define Base Class
class Bird:
    type = "Bird"

    # Write Constructor
    def __init__(self, name):
        self.name = name

    # Write Methods
    def getName(self):
        return self.name

    # This is a base class method
    def fly(self):
        return "{} is now flying".format(self.name)
    
# Define Sub Classes of Birds
class Penguin(Bird):
    species = "Penguin"

    # This method overwrites the parent method
    def fly(self):
        return "Penguins can't fly."

class Dodo(Bird):
    species = "Dodo"
    
    def fly(self):
        return "Dodos are extinct"
    

penguin1 = Penguin("Tony")

# Example of classing Penguin1's fly method
print(penguin1.fly())
print(penguin1.getName())
