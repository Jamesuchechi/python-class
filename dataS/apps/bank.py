class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return self.balance
        
    def get_balance(self):
        return self.balance
    
account = BankAccount(10000)
print(account.get_balance)
account.deposit(2000)
print(account.get_balance)

