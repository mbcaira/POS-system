from datetime import date

#Holds all the members fromn the current session
Members = []

class Membership:
    def __init__(self, name, memNumber, expiry):
        self.memNumber = memNumber
        self.name = name
        self.expiry = expiry
        self.expired = False
        Members.append(self)
    
    #Checks if the membership is expired or not
    def memberCheck(self):
        if (self.expiry < date.today()):
            self.expired = True
        else:
            self.expired = False

    




