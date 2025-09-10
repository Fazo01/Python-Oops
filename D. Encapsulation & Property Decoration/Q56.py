# 56. Creatgite a `Product` class with private stock quantity and a method to restock.
class Product:
  def __init__(self,name,stock):
    self.name=name
    self.__stock=stock
  @property
  def stock(self):
    return self.__stock
  def restock(self,amount):
    if amount>0:
      self.__stock+=amount
    else:
      raise ValueError("Restock amount must be positive")
  def sell(self,amount):
    if 0<amount<=self.__stock:
      self.__stock-=amount
    else:
      raise ValueError("Not enough stock")

p1=Product("Muhammad Faizan",900)
p1.restock(90)
p1.sell(9)
print(p1.stock)