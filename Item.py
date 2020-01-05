# Global tax rate
taxRate = 0.13


# Data fields used for the item class
class Item:
    def __init__(self, info):
        self.number = info[0:4]
        self.intNumber = int(self.number.strip())
        self.name = info[8:19].strip()
        self.price = info[24:30]
        self.floatPrice = float(self.price.strip())
        self.taxed = info[32].strip()
        if self.taxed == "N":
            self.tax = 0.00
        else:
            self.tax = taxRate * self.floatPrice

    # Method to pull item data from the inventory list and make an item object
    def check_inventory(number, items):
        # Search up item input using item number and if it exists on the inventory list, make an item object
        for i in items:
            if i.intNumber == number:
                return i
        else:
            print("ITEM NOT FOUND")







