# Account class with acno, customername, balance with methods 
# deposit, withdraw and getbalance 

class Account:
    def __init__(self, acno, customername, balance=0):
        self.acno = acno
        self.customername = customername
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            raise ValueError("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
        else:
            raise ValueError("Insufficient funds or invalid withdrawal amount.")

    def get_balance(self):
        return self.balance
    

