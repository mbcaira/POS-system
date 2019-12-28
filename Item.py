# Global tax rate
taxRate = 1.13


# Data fields used for the item class
class Item:
    def __init__(self, info):
        self.number = info[0:4]
        self.intNumber = int(self.number)
        self.name = info[8:19]
        self.price = info[24:30]
        self.intPrice = float(self.price)
        self.taxed = info[32]
        if self.taxed == "N":
            self.tax = 0.0
        else:
            self.tax = taxRate * self.intPrice

    # Method to pull item data from the inventory list and make an item object
    def check_inventory(number, items):
        # Search up item input using item number and if it exists on the inventory list, make an item object
        for i in items:
            if i.intNumber == number:
                return i
        else:
            print("ITEM NOT FOUND")







