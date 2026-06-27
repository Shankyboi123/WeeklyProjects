class BankAccount:

    def __init__(self, type: str, balance = None):
        self.name = type
        self.balance = balance or 0 
    
    def AccountType(self):
        return self.name
    
    def BankBalance(self):
        return self.balance
    
    def BankDeposit(self, deposit):
        x = self.balance
        self.balance += deposit
        return print(f"New Bank Balance is {self.balance}")
    
    def BankWithdraw(self, withdraw):
        if self.balance - withdraw < 0: 
            return print("Insufficent funds")
        else: 
            self.balance -= withdraw

            return print(f"{withdraw} has been withdrawn.")

class SavingsAccount(BankAccount):
    def apply_interest(self, rate:float):
        if rate > 1 or rate < 0: 
            return print("Enter a valid rate")
        else: 
            self.balance = float(1 + rate) * self.balance 
            return print(f"Interest has accured at a rate of {rate}%")
        
class Customer:
    def __init__(self, name):
        self.name = name 
        self.accounts = []

    def open_account(self, Account):
        self.accounts.append(Account) 
    
    def account_statement(self):
        for i in range(len(self.accounts)):
            print(f"{self.accounts[i].AccountType()}: {self.accounts[i].BankBalance()}")
    
    def AccountName(self):
        return self.name

class Bank: 
    def __init__(self):
        self.customers = []
    
    def new_customer(self, Customer):
        self.customers.append(Customer)
    
    def customerbalances(self):
        for i in range(len(self.customers)):
            print(f"{self.customers[i].AccountName()}:")
            self.customers[i].account_statement()

        

if __name__ =="__main__":
    Everyday = BankAccount(type= "Transaction", balance=1000)
    Everyday.BankWithdraw(1100)
    Everyday.BankWithdraw(100)
    Everyday.BankDeposit(100)
    
    Savings = SavingsAccount(type="Savings", balance=500)
    Savings.apply_interest(0.054)

    shshank = Customer(name="Shshank")
    shshank.open_account(Savings)
    shshank.open_account(Everyday)

    shshank.account_statement()

    nab = Bank()

    nab.new_customer(shshank)

    nab.customerbalances()






