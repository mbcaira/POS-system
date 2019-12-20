import Membership
import datetime

receipt = ["**NO ITEMS**"]
class Receipt:

    def addItem(self, item):
        receipt.remove("**NO ITEMS**")
        receipt.append(item)

    def voidItem(self, item):
        k = receipt.index(item)
        if (k == null):
            print("No item found")
        else:
            receipt.remove(item)

    def softTotal(self, receipt):
        softTotal = 0
        for x in self.receipt:
            softTotal += self.receipt[x].price
            softReceipt = ("TOTAL:   "+softTotal)

    def finalTotal(self, receipt):
        totalPrice = 0
        totalReceipt = "ITEM           PRICE\n"
        for x in self.receipt:
            totalReceipt += (self.receipt[x]+"          "+self.receipt[x].price+"\n")
            totalPrice += self.receipt[x].price
        total.receipt += ("TOTAL:    "+totalPrice+"\n")
        totalAfterTax = totalPrice * 1.13
        totalReceipt += ("TOTAL:    "+totalAfterTax+"\n")
        return totalReceipt
