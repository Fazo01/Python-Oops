# 15. Implement a class `Bank` that stores multiple accounts and allows transfers between them.
class Bank:
  def __init__(self):
    self.accounts={}
  def createAccount(self,name,balance=0):

    account_number=len(self.accounts)+1
    self.accounts[account_number]={'name':name,'balance':balance}

  def deposite(self,account_number,amount):
    self.accounts[account_number]['balance']+=amount
  def withdraw(self,account_number,amount):
    self.accounts[account_number]['balance']-=amount
  def transfer(self,from_account,to_account,amount):
    self.accounts[from_account]['balance']-=amount
    self.accounts[to_account]['balance']+=amount
  def show_account(self):
    for acc_num,acc_info in self.accounts.items():
      print(f"Account {acc_num}: {acc_info['name']} - ${acc_info['balance']}")
b1=Bank()
b1.createAccount("Muhammad",1000)
b1.show_account()
b1.deposite(1,100)
b1.show_account()
b1.createAccount("Faizan",1000)
b1.show_account()
b1.deposite(2,900)
b1.show_account()
b1.transfer(1,2,900)
b1.show_account()
b1.withdraw(2,2600)
b1.show_account()