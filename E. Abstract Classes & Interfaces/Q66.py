# 66. Write an abstract class `Account` with `deposit()` and `withdraw()` methods.
from abc import ABC,abstractmethod
class Account(ABC):
  def __init__(self,balance=0):
    self.balance=balance
  @abstractmethod
  def deposite(self,amount):
    pass
  @abstractmethod
  def withdraw(self,amount):
    pass
class SavingsAccount(Account):
  def deposite(self, amount):
    if amount>0:
      self.balance+=amount
      print(f"Deposite amount {amount} new balance {self.balance}")
    else:
      print("Amount should be in positive")
  def withdraw(self, amount):
    if 0<amount<self.balance:
      self.balance-=amount
      print(f"Withdraw amount {amount} new balance {self.balance}")
    else:
      print("Insufficient Value")
class CurrentAccount(Account):
  def deposite(self, amount):
    if amount>0:
      self.balance+=amount
      print(f"Deposite amount {amount} new balance {self.balance}")
    else:
      print("Amount should be in positive")
  def withdraw(self, amount):
    if 0<amount<self.balance:
      self.balance-=amount
      print(f"Withdraw amount {amount} new balance {self.balance}")
    else:
      print("Insufficient Value")

Account=[SavingsAccount(1000),CurrentAccount(100)]
for i in Account:
  i.deposite(1000)
  i.withdraw(100)