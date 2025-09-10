# 58. Implement a `BankAccount` class that logs every change to balance.
class BankAccount:
  def __init__(self,owner,balance=0):
    self.owner=owner
    self.balance=balance
    self.log=[f"Account created with {balance}"]#list
  def deposite(self,amount):
    self.balance+=amount
    self.log.append(f"Deposited {amount}, balance = {self.balance}")#attached with __init__ log
  def withdrawal(self,amount):
    if amount<=self.balance:
      self.balance-=amount
      self.log.append(f"Withdrawal {amount}, balance={self.balance}")
    else:
      self.log.append(f"Failed withdrawal of {amount}")
b1=BankAccount("Muhammad Faizan",9000)
b1.deposite(1000)
print(b1.log)