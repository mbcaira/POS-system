from datetime import *

# Fetches today's date
today = date.today()

# Initializes membership numbers
membershipNumbers = 1000001

# Holds all the members from the current session
Members = []


class Membership:
    
    def __init__(self, name):
        global membershipNumbers
        self.memNumber = membershipNumbers
        membershipNumbers += 1  # Incremement the global membership number for this session
        self.name = name
        self.expiry = today
        self.expired = False

        # Writing new member to membership database & checking if there is already an existing membership
        expiry_string = self.expiry.strftime("%m/%d/%y")
        mem_number_string = str(self.memNumber)
        mem_info = ""
        with open ("Members.txt", "a+") as preMembers:
            # Checks to see if the new member already exists on file, and if they do, return an error message
            with open ("Members.txt") as preCheck:
                if self.name in preCheck.read():
                    print("Error: Name exists within database, cannot make a new membership")
                else:
                    mem_info = (mem_info + mem_number_string + " " + self.name + " " + expiry_string + "\n")
                    preMembers.write(mem_info)

    # Checks if the membership is expired or not

    def member_check(self):
        if self.expiry < today:
            self.expired = True
        else:
            self.expired = False




