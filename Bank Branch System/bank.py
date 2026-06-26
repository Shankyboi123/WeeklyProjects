class BankAccount:

    def __init__(self, balance = None):
        self.balance = balance or 0 
    
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
    def __init__(self, Accounts: list):
        self.
        

if __name__ =="__main__":
    Everyday = BankAccount(balance=1000)
    Everyday.BankWithdraw(1100)
    Everyday.BankWithdraw(100)
    Everyday.BankDeposit(100)
    
    Savings = SavingsAccount(balance=500)
    Savings.apply_interest(0.054)






