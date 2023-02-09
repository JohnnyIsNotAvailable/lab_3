class Account:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance
        
    def deposit(self, dep):

        self.balance += dep
        print('Deposit Accepted')
        
    def withdraw(self, wd):
        if self.balance >= wd:
            self.balance -= wd
            print('Withdrawal Accepted') 
        else:
            print('Insufficient funds')



s = Account(input('Enter your name: '), int(input('Enter the replenishment amount: ')))
s.deposit(int(input("Enter the deposit replenishment amount: ")))
s.withdraw(int(input("Enter the withdrawal replenishment amount: ")))
