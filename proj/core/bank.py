# Savings Account, Current Account
# SA if the b < amount = Should not allow
class InsufficientBalanceError(Exception):
    pass

class Account():
    def __init__(self, n, b, t):
        self.n = n
        self.b = b
        self.t = t
    def credit(self, amount):
        self.b += amount
    def debit(self, amount):
        self.b -= amount

class SA(Account):
    def __init__(self, n, b=1000):
        Account.__init__(self, n, b, 'S')
    def debit(self, amount):
        if self.b >= amount:
            Account.debit(self, amount)
        else:
            raise InsufficientBalanceError('Insufficient balance')

class CA(Account):
    def __init__(self, n, b=0):
        Account.__init__(self, n, b, 'C')