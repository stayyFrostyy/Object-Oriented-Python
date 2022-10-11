
# Data Encapsulation used within Classes

# Define Class
class Laptop:

    # Write Constructor
    def __init__(self):
        # Set initial attribute
        self.__maxprice = 500
    
    # These methods can also be known as get-set methods
    # Define methods for getting attributes
    def sell(self):
        print("You sold LAPTOP for {} squids.".format(self.__maxprice))

    # Define methods for setting attributes
    def setPrice(self, price):
        self.__maxprice = price


# Instantiate Class
item = Laptop()
item.sell()
# Output: "You sold LAPTOP for 500 squids."

# Attempt to modify item's attribute
item.__maxprice = 1000
item.sell()
# Output: "You sold LAPTOP for 500 squids."

# Set item's attribute using set method
item.setPrice(1000)
item.sell()
# Output: "You sold LAPTOP for 1000 squids."