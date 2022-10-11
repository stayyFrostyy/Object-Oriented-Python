
# Example of very basic class in python

# Defining class name
class Parrot:

    # Known as class attribute
    species = "bird"

    # Known as instance attribute
    # AKA Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age


# Instantiating the Parrot Class
plum = Parrot("Plum", 15)
tonk = Parrot("Tonk", 3)

# Accessing class attributes
print("Tonk is a {}.".format(tonk.__class__.species))

# Accessing instance attributes
print("plum is {} years old.".format(plum.age))

# Accessing all attributes
print("{} is a {} year old {}.".format(tonk.name, tonk.age, tonk.__class__.species))

