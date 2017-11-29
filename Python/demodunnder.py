




class Account:
    def __init__(self, balance=0, interest=0.001):
        self.balance = balance
        self.interest = interest
        self.transaction = []

    def withdraw(self, amount):
        if amount > self.balance

    def __str__(self):
        return f'Balance: {self.balance}, interest: {self.interest}'

    def __repr__(self):
        return f'Account({self.balance}, {self.interest})'

    def __eq__(self, other):
        if type(other) is float:
            print('other is float')
            return self.balance == other
        elif type(other) is Account:
            print('other is account')
            return self.balance == other.balance
        raise TypeError('invalid type '+ str(type(other)))

    def __ne__(self, other):
        return self.balance != other.balance

    def __le__(self, other):
        return self.balance <= other.balance

acc_a = Account(100.0)
#print(acc.balance)

print(acc_a.__repr__())


