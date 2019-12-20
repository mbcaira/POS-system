from datetime import date

class Membership:
    def __init__(self, memNumber, name, expiry):
        self.memNumber = memNumber
        self.name = name
        self.expiry = expiry
        self.expired = False
    
    def memberCheck(self):
        if (self.expiry < date.today()):
            self.expired = True
        else:
            self.expired = False

