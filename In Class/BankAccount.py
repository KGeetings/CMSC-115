class BankAccount:
    def __init__(self, owner, startingBalance):
        self.owner = owner
        self.balance = startingBalance
        self.interestRate = .05

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance = self.balance - amount
        else:
            print("OVERDRAFT!!!")
            self.balance -= 50
    
    def deposit(self, amount):
        self.balance += amount

    def addMonthlyInterest(self):
        newInterest = self.interestRate * self.balance / 12
        self.balance += newInterest
    
    def transfer(self, other, amount):
        if self.balance >= amount:
            self.balance -= amount
            other.balance += amount
        else:
            print("OVERDRAFT")
            self.balance -= 50
    def getBalance(self):
        return self.balance
    def getOwner(self):
        return self.owner

a = BankAccount("Kenyon", 40000)
b = BankAccount("Fido", 250)

b.withdraw(75)

a.addMonthlyInterest()
b.addMonthlyInterest()

a.transfer(b, 600)

print(f"{a.getOwner} has ${a.getBalance}.")
print(f"{b.getOwner} has ${b.getBalance}.")