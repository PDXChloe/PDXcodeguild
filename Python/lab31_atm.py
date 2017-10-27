
class AtmAccount:

    def __init__(self, balance=0, interest_rate=0.001):
        self.balance = balance #set this variable to itself and then set the def__init__ variable to default amount.
        self.interest_rate = interest_rate
        self.transactions = []
        #print("account balance: $" + str(balance))

    def check_balance(self):
        return self.balance


    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f'user deposited: ${amount}')

    def check_withdraw(self, amount):
        return self.balance - amount >= 0

    def withdraw(self, amount):
        self.balance -= amount
        self.transactions.append(f'user withdraw: ${amount}')

    def calc_interest(self):
        amount_interest = float(self.balance) * self.interest_rate
        return amount_interest

    def print_transactions(self):
        for transaction in self.transactions:
            print(transaction)

amount = input("Enter the amount of money to make a new account")
new_account = AtmAccount(int(amount), 0.001)

while True:

    command = input("What would you like to do (deposit (d), withdraw (w), check balance (cb), history (h) or quit (q)?").lower()
    if command == 'quit' or command == 'q':
        print("Goodbye")
        break

    if command == 'deposit' or command == 'd':
        amount = input("How much would you like to deposit?")
        new_account.deposit(int(amount))
        print(f'account balance: ${new_account.balance}.')

    if command == 'withdraw' or command == 'w':
        amount = input('How much would you like to withdraw?')
        if new_account.check_withdraw(int(amount)) == False:
            print(f'${amount} is over your current balance of: ${new_account.balance}.')
        else:
            new_account.withdraw(int(amount))
            print(f'You have withdrawn: ${amount}.\nCurrent balance: ${new_account.check_balance()}.')

    if command == 'check balance' or command == 'cb':
        print(f'Balance: {new_account.check_balance()}')

    if command == 'history' or command == 'h':
        new_account.print_transactions()



