
class BankAccount:
    def __init__(self, name_input, int_rate=0.001, bal = 0):
        self.name = name_input
        self.int_rate = int_rate
        self.balance = bal
        
    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Funds: Charging $5 fee")
            self.balance = self.balance - 5
        else:
            self.balance -= amount
        return self

    def display_account_info(self):
        print(f"Current {self.name} Balance: {self.balance}")
        return self

    def yield_interest(self):
        self.balance += self.balance * self.int_rate
        return self

#create instances of class BankAccount
checking = BankAccount('Checking',0.001)
savings = BankAccount('Savings',bal=1000)

#print beginning balances
print(f"Beginning Checking Balance: {checking.balance}")
print(f"Beginning Savings Balance: {savings.balance}")

checking.deposit(100).deposit(100).deposit(100).withdraw(40).yield_interest().display_account_info()
savings.deposit(200).deposit(200).withdraw(30).withdraw(50).withdraw(90).withdraw(100).yield_interest().display_account_info()