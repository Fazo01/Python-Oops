# 60. Write a `Car` class with property to check if fuel is low.
class Car:
  def __init__(self,fuel):
    self.__fuel=fuel
  @property
  def fuel(self):
    return self.__fuel
  def checkFuel(self):
    if 15<self.__fuel<100:
      print(f"Fuel tank is about {self.__fuel}% full so it's considered a good capacity")
    else:
      print("Fuel is low")
c=Car(90)
c.checkFuel()