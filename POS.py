import Item
import Membership
import Receipt
from datetime import datetime

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
    if membership_number in members:
        print("Please enter an item number: ")


    else:
        print("Error, membership does not exist. Would you like to sign them up? (Y/N): ")
        sign_up = input()
        sign_up.upper()
        if "Y" in sign_up:
            print("Please enter the member's name: ")
            member_name = input()
            member_name.lower().capitalize()
            Membership.Membership(member_name)

        elif "N" in sign_up:
            print("Transaction completed, have a nice day!\n")
            in_transaction = False

        else:
            print("Error, invalid selection\n")





