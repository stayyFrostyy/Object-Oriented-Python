
# Example of Polymorphism in Python using Classes

# Define classes
class Parrot:
    
    # Define methods
    def fly(self):
        print("Parrots can fly")
    
# Define class with same methods but different definition
class Penguin:

    # Same method name as Parrot Class
    def fly(self):
        print("Penguins can't fly")

class Bear:
    def fly(self):
        print("Bears don't have wings lol")


# Depending on class type of 'bird', different method will be called
# Function CANNOT be called on objects without a 'fly' method
def fly_test(bird):
    bird.fly()

# Instantiate objects
parrot1 = Parrot()
penguin1 = Penguin()
bear1 = Bear()

# Try function with each object.
fly_test(parrot1)
fly_test(penguin1)
fly_test(bear1)