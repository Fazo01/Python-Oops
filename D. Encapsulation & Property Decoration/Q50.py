# 50. Create a `Car` class with private speed and a method to accelerate/decelerate.
class Car:
  def __init__(self,brand,speed=0):
    self.brand=brand
    self.__speed=speed
  @property
  def speed(self):
    return self.__speed
  @speed.setter
  def speed(self,value):
    if value>=0:
      self.__speed=value
    else:
      print("Value should be positive")
  def accelerate(self,amount):
    if amount>0:
      self.__speed+=amount
      print(f"{self.brand} accelerated by amount {amount}. Current speed {self.__speed}")
    else:
      print("Insufficient value")
  def decelerate(self,amount):
    if 0<amount<self.__speed:
      self.__speed-=amount
      print(f"{self.brand} decelerated by amount {amount}. Current speed {self.__speed}")
    else:
      print("Insufficient value")
c1=Car("Toyota",90)
c1.accelerate(90)
c1.decelerate(9)  