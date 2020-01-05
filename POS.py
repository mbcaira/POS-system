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
in_inventory = None
while in_transaction is True:

    # Checking if the inputted membership number corresponds to a membership on file
    membership_number_string = str(membership_number)
    member_database = members.read()
    if membership_number_string in member_database:
        membership_number_string = str(membership_number)

        # Initialize receipt/transaction mode
        member_receipt = Receipt.Receipt(membership_number_string)
        end_of_order = False
        while end_of_order is False:
            print("Please enter an item number: ")
            item = input()
            # Prints the receipt of the order
            if item.upper() == "N":
                final_receipt = member_receipt.finalize_receipt()
                print(final_receipt)
                print("Thank you for shopping, have a nice day!")
                end_of_order = True
            elif item.upper() == "VOID":
                print("Enter an item number to void: ")
                # Checks if the entered item number exists in the inventory and if so, calls the remove_receipt function
                # and prints a confirmation message
                item = input()
                item = int(item)
                for i in Items:
                    if item == i.intNumber:
                        member_receipt.remove_item(i)
            else:
                # Checks if the entered item number exists in the inventory and if so, displays its name and price
                # and adds it to the receipt
                item = int(item)
                for i in Items:
                    if item == i.intNumber:
                        member_receipt.add_item(i)
                        in_inventory = True
                        break
                    else:
                        in_inventory = False
                if in_inventory is False:
                    print("No item found")

            # End transaction status
            in_transaction = False

    else:
        # Gives cashier the option to sign up a new member
        print("Error, membership does not exist. Would you like to sign them up? (Y/N): ")
        sign_up = input().upper()
        if sign_up == "Y":
            print("Please enter the member's name: ")
            member_name = input()
            member_name.lower().capitalize()
            newMem = Membership.Membership(member_name)
            membership_number = newMem.memNumber

        elif sign_up == "N":
            print("Transaction completed, have a nice day!\n")
            in_transaction = False

        else:
            print("Error, invalid selection\n")