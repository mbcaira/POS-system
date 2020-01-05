from datetime import *


class Receipt:
    def __init__(self, member_number):
        # Initialize the receipt as a list for future modifications (adding and removing items)
        self.member_items = []
        self.member_number = member_number
        self.total = 0.0
        self.total_tax = 0.0

    # Adds items to the member's receipt and displays the current total with tax
    def add_item(self, item):
        self.member_items.append(item)
        item_price = item.floatPrice
        self.total_tax += item.tax
        self.total += item_price + item.tax
        print("{0:<20} {1:>10}".format(item.name, str(item.floatPrice)))
        print("TAX: %26.2f" % (self.total_tax))
        print("TOTAL: %24.2f" % (self.total))

    # Removes items from the receipt and displays the current total with tax
    def remove_item(self, item):
        if item in self.member_items:
            self.member_items.remove(item)
            self.total_tax -= item.tax
            self.total -= item.floatPrice
            print("REMOVED")
            print("{0:<20} {1:>10}".format(item.name, str(item.floatPrice)))
            print("TAX: %26.2f" % (self.total_tax))
            print("TOTAL: %24.2f" % (self.total))

        elif len(self.member_items) == 0:
            print("No items in the receipt")

        else:
            print("Item does not exist in member's receipt")

    # Finalizes the receipt string and returns it to the POS
    def finalize_receipt(self):
        # Initialize the receipt string
        final_receipt = "             RECEIPT\nMembership Number: " + (self.member_number + "\n")
        total = 0.0
        total_tax = 0.0
        final_receipt += "ITEMS:\n"
        for item in self.member_items:
            final_receipt += ("{0:<20} {1:>10}\n".format(item.name, str(item.floatPrice)))
            total_tax += item.tax
            total += total_tax + item.floatPrice
        final_receipt += ("\nTAX: %26.2f\n" % (self.total_tax))
        final_receipt += ("TOTAL: %24.2f\n" % (self.total))
        final_receipt += str(date.today())
        return final_receipt
