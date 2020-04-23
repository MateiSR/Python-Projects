from random import randint

class BankAccount:

    def __init__(self, owner, age):
        self.owner = owner
        self.age = int(age)
        self.balance = randint(250, 500)
        self.debt = randint(500, 2500)
        self.interestRate = randint(2, 10)
        self.Names = self.owner.split(' ')
        self.Names.append(' ' * 3) # In case only one name is provided
        self.first_name = self.Names[0]
        self.last_name = self.Names[1]

    def getBalance(self): # Get current balance
        print(f'Your current balance is ${self.balance}.')
        return self.balance

    def getDebt(self): # Get current debt
        print(f'You currently ${self.debt} to the bank.')
        return self.debt

    def withdraw(self, amount): # Withdraw specific amount
        if amount <= self.balance:
            self.balance -= amount
            print(f'You withdrew ${amount}. Your remaining balance is ${self.balance}.')
            return self.balance
        else:
            print(f'Your account doesn\'t have enough money. Current balance: ${self.balance}.')
            return None

    def deposit(self, amount): # Deposit specific amount
        self.balance += amount
        print(f'You have deposited ${amount} into your bank account. Your new balance is ${self.balance}.')
        return self.balance

    def payDebt(self, amount): # Repay debt
        if self.balance <= amount and self.debt <= amount:
            self.balance -= amount
            self.debt -= amount
            print(f'Remaining debt: ${self.debt}; Remaining balance: ${self.balance}')
            return self.debt
        if self.balance < amount:
            print(f'Your current balance: ${self.balance}. Needed money: ${amount - self.balance}.')
            return self.balance
        if amount > self.debt:
            print(f'You have deposited more money than your debt requires.')
            return self.debt

    def getIntRate(self): # Debt interest rate
        print(f'Interest rate: {self.interestRate}%')
        return self.interestRate

    def __del__(self):
        print(f'Deleted account {self.owner}.')


class Bank(BankAccount):

    def __init__(self, name, address, state, owner):
        self.name = name
        self.address = str(address)
        self.state = state
        self.owner = owner
        self.safeMoney = randint(7500, 25000)
        self.intRate = randint(2, 10)
        self.providedDebts = randint(10000, 150000)
        self.bussinessId = f'ROM{randint(300000, 700000)}'

    def getSafe(self): # Get safe balance
        print(f'Current balance in safe: ${self.safeMoney}')
        return self.safeMoney

    def addToSafe(self, amount): # Add money to safe
        self.safeMoney += amount
        print(f'Added ${amount} to safe. New balance: ${self.safeMoney}')
        return self.safeMoney

    def bussinessInfo(self): # Bussiness info
        print(f'Name: {self.name}; Address: {self.address}; State: {self.state}; Safe balance: ${self.safeMoney}; Bussiness ID: {self.bussinessId}')
        return self.bussinessId

    def bankIntRate(self): # Bank official int rate
        print(f'Official interest rate provided by bank is {self.intRate}%')
        return self.intRate

    def getDebts(self): # Total debts
        print(f'Account owners currently owe ${self.providedDebts}.')
        return self.providedDebts

    def __del__(self):
        print(f'Bussiness ID {self.bussinessId} succesfully removed from database.')
