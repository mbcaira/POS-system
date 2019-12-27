#Global tax rate
taxRate = 1.13

#Data fields used for the item class
class Item:
    def __init__(self, number, name, price, taxed):
        self.number = number
        self.name = name
        self.price = price
        self.taxed = taxed
        if self.taxed == "N":
            self.tax = 0
        else:
            self.tax = taxRate*self.price
    
    #Method to pull item data from the inventory list and make an item object
    def checkInventory(self):
        inv = open("inventory.txt", "r")
        inventory = []
        for i in inv:
            inventory.append(i)
        #Removes text headers
        inventory.pop(0)
        
        #Search up item input using item number and if it exists on the inventory list, make an item object
        if self.number in inventory:
            
            #Gather item info from inventory array if the item exists
            number = self.number
            itemPos = inventory.index(number)
            name = inventory[itemPos][9:19]
            price = inventory[itemPos][25:30]
            taxed = inventory[itemPos][33]

            memberItem = Item(number, name, price, taxed)
            return(memberItem)
        else:
            print("ITEM NOT FOUND")

            


    

        
