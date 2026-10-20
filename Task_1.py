class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance < amount:
            print('Insufficient funds')
            return
        self.balance -= amount

    def check_balance(self):
        return self.balance

acc = BankAccount('Ahmed', 1000)
acc.withdraw(200)
print(acc.check_balance())
acc.deposit(300)
print(acc.check_balance())
acc.withdraw(1200)
print(acc.check_balance())
