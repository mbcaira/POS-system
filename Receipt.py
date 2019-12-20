import Membership
import Item
import datetime

#Receipt class that summarizes the member's order

#Initialize the receipt array
receipt = ["**NO ITEMS**"]
class Receipt:

    #Adds an item to the receipt array
    def addItem(self, item):
        receipt.remove("**NO ITEMS**")
        receipt.append(item)

    #Removes an item from the receipt array
    def voidItem(self, item):
        k = receipt.index(item)
        if (k == None):
            print("No item found")
        else:
            receipt.remove(item)

    #Calculates the total cost of the order before tax at the current point and returns the receipt as a string
    def softTotal(self, receipt):
        softTotal = 0
        for x in self.receipt:
            softTotal += self.receipt[x].price
            softReceipt = ("TOTAL:   "+softTotal)
            return softReceipt

    #Calculates the final total price of the order with tax and returns the final receipt as a string
    def finalTotal(self, receipt):
        #initializes totals as 0
        totalPrice = 0
        totalTax = 0
        totalAfterTax = 0
        totalReceipt = "________________"
        totalReceipt = "|ITEM     PRICE|\n"
        
        #Finds the total price of the current order before tax
        for x in self.receipt:
            totalReceipt += (self.receipt[x]+"          "+self.receipt[x].price+"\n")
            totalPrice += self.receipt[x].price
        totalReceipt   += ("| TOTAL:    "+totalPrice+" |\n")

        #Finds the total tax applicable to the current order
        for y in self.receipt:
            totalTax += self.receipt[y].tax
    
        totalReceipt    += ("| TAX:       "+totalTax+"|\n")
        totalAfterTax = totalTax + totalPrice    
        totalReceipt    += ("| TOTAL:    "+totalAfterTax+"|\n")
        totalReceipt    += ("|______________|")
        return totalReceipt
