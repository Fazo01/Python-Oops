# 46. Implement a `BankAccount` class with private balance and getter/setter methods.
class BankAccount:
  def __init__(self,owner,balance=0):
    self.owner=owner
    self.__balance=balance

  @property
  def balance(self):
      return self.__balance
  
  @balance.setter
  def balance(self,amount):
    if amount>=0:
       self.__balance=amount # for getting new value
      
    else:
       print("Balance should be in positive")

  def deposite(self,amount):
    if amount>0:
        self.__balance+=amount
        print(f"Deposited balance: {amount} \nNew balance: {self.__balance}")
    else:
        print("Balance should be in positive")

  def withdrawal(self,amount):
    if self.__balance>=amount:
        self.__balance-=amount
        print(f"Widthrawal amount: {amount}\nNew balance: {self.__balance}")
    else:
      print("Insufficient balance")
b1=BankAccount("Muhammad Faizan",9000)
b1.withdrawal(10000)
b1.deposite(9000)
b1.balance=5000
print(b1.balance)