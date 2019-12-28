import Membership
import Item
from datetime import *

today = date.today()


# Receipt class that summarizes the member's order

class Receipt:

    # Initialize the receipt array
    def __init__(self, member):
        receipt = {self.member.memNumber}
        receipt.append("**NO ITEMS**")

    # Adds an item to the receipt array
    def addItem(self, item):
        self.receipt.remove("**NO ITEMS**")
        self.receipt.append(item)

    # Removes an item from the receipt array
    def voidItem(self, item):
        k = self.receipt.index(item)
        if k == None:
            print("No item found")
        else:
            self.receipt.remove(item)

    # Calculates the total cost of the order before tax at the current point and returns the receipt as a string
    def soft_total(self, receipt):
        soft_total = 0
        for x in self.receipt:
            soft_total += self.receipt[x].price
            soft_receipt = ("TOTAL:   " + soft_total)
            return soft_receipt

    # Calculates the final total price of the order with tax and returns the final receipt as a string
    def finalTotal(self, receipt):
        # initializes totals as 0
        total_price = 0
        total_tax = 0
        total_after_tax = 0
        total_receipt = "________________"
        total_receipt = "|ITEM     PRICE|\n"

        # Finds the total price of the current order before tax
        for x in self.receipt:
            total_receipt += (self.receipt[x] + "          " + self.receipt[x].price + "\n")
            total_price += self.receipt[x].price
        total_receipt += ("| TOTAL:    " + total_price + " |\n")

        # Finds the total tax applicable to the current order
        for y in self.receipt:
            total_tax += self.receipt[y].tax

        total_receipt += ("| TAX:       " + total_tax + "|\n")
        total_after_tax = total_tax + total_price
        total_receipt += ("| TOTAL:    " + total_after_tax + "|\n")
        total_receipt += "|______________|"
        return total_receipt
