from decimal import *

class Record:
    def __init__(self,change,note,timestamp=None,op=None,tally=None,balance=None):
        self.change=Decimal(str(change))
        self.note=note
        self.timestamp=timestamp
        self.op=op
        self.tally=tally
        self.balance=balance
    


