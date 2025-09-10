# 49. Implement a `Product` class with price validation using property decorators.
class Product:
  def __init__(self,name,price):
    self.name=name
    self.__price=None
    self.price=price

  @property
  def price(self):
    return self.__price
  
  @price.setter
  def price(self,value):
    if value>=0:
      self.__price=value
    else:
      print("Price cannot be negative")

  def display(self):
    print(f"{self.name} => Price:{self.__price}")

p1=Product("Muhammad Faizan",-900)
p1.display()
