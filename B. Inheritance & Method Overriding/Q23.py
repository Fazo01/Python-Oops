# 23. Write a class `Account` inherited by `SavingsAccount` and `CurrentAccount` with different withdrawal rules.
class Account:
  def __init__(self,acc_holder,balance):
    self.acc_holder=acc_holder
    self.balance=balance

  def deposit(self,amount):
      self.balance+=amount
      print(f"Your deposit balance {amount}")

  def withdrawal(self,amount):
      if amount<= self.balance:
        self.balance-=amount
        print(f"Withdrawal money : {amount} \nRemaning money: {self.balance}")
      else:
        print("Balance is insufficient")

  def showBalance(self):
      print(f"Account holder: {self.acc_holder}\nYour balance is {self.balance}")

class SavingsAccount(Account):
  def __init__(self, acc_holder,balance,min_balance=1000):
    super().__init__(acc_holder,balance)
    self.min_balance=min_balance
  def withdrawal(self, amount):
    if self.balance -amount>=self.min_balance:
       self.balance-=amount
       print(f"Withdrawal amount: {amount}\nremainig amount: {self.balance}")
    else:
       print(f"Insufficient balance. Min balance is {self.min_balance}")
  
class CurrentAccount(Account):
  def __init__(self, acc_holder,balance,overdraft_limit=1000):
    super().__init__(acc_holder,balance)
    self.overdraft_limit=overdraft_limit
  def withdrawal(self, amount):
      if self.balance-amount >= -self.overdraft_limit:
        self.balance-=amount
        print(f"Withdarawl {amount} Overdraft is allowed. Balance {self.balance}")
      else:
        print(f"Withdrawal denied. Overdraft limit of {self.overdraft_limit} exceeded") 


a=Account("Muhammad Faizan",1000)
a.deposit(100)
a.showBalance()
a.withdrawal(1100)
a1=CurrentAccount("Muhammad Faizan",1000)
a1.withdrawal(2100)