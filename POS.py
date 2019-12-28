import Item
import Membership
import Receipt

# Initialize inventory
Inventory = []
inventoryFile = open("Inventory.txt", "r")
for i in inventoryFile:
    Inventory.append(i)

# Remove inventory text headers from inventory array
Inventory.pop(0)

# Generate an array of Item objects for convenience during the transaction
Items = []
for i in Inventory:
    newItem = Item.Item(i)
    Items.append(newItem)

# Initialize membership datafile
members = open("Members.txt", "r")

# POS user interactions
print("Please enter a membership number: ")
membership_number = input()

# Entering transaction
in_transaction = True
while in_transaction is True:

    # Checking if the inputted membership number corresponds to a membership on file
    membership_number_string = str(membership_number)
    if membership_number_string in members.read():

        # Initialize receipt
        member_receipt = Receipt.Receipt(membership_number)
        print("Please enter an item number: ")
        item = input()

        for i in Items:
            if item == i.intNumber:
                member_receipt.add_item(item)

        # End transaction
        in_transaction = False

    else:
        print("Error, membership does not exist. Would you like to sign them up? (Y/N): ")
        sign_up = input()
        sign_up.upper()
        if sign_up is "Y":
            print("Please enter the member's name: ")
            member_name = input()
            member_name.lower().capitalize()
            newMem = Membership.Membership(member_name)
            membership_number_string = newMem.memNumber

        elif sign_up is "N":
            print("Transaction completed, have a nice day!\n")
            in_transaction = False

        else:
            print("Error, invalid selection\n")





