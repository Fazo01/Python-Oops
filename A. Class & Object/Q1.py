# 1. Create a class `BankAccount` with methods to deposit, withdraw, and check balance. Prevent withdrawals if balance is insufficient.
class BankAccount:
  def __init__(self):
    self.balance=0
  def deposit(self,amount):
    if amount>0:
      self.balance+=amount
      print(f"Deposited amount : {amount}")
    else:
      print("Amount should be in positive")

  def withdraw(self,amount):
    if amount>self.balance:
      print("Entered amount is insufficient")
      
    elif amount<=0:
      print("value should be in postive")
    else:
      self.balance-=amount
      print(f"remaining balance is {self.balance}")
      
  def checkbalance(self):
    print(f"Present balance is :{self.balance}")
customer1=BankAccount()
customer1.deposit(2000)
customer1.withdraw(1000)
customer1.checkbalance()
customer1.withdraw(0)
customer1.checkbalance()
