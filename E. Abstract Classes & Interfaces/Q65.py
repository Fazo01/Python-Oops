# 65. Implement an abstract class `Device` with subclasses `Phone` and `Laptop`.
from abc import ABC,abstractmethod
class Device(ABC):
  def __init__(self,brand,model):
    self.brand=brand
    self.model=model
  @abstractmethod
  def power_on(self):
    pass
  @abstractmethod
  def power_off(self):
    pass
class Phone(Device):
  def power_on(self):
    return f"{self.brand} {self.model} phone is now on"
  def power_off(self):
    return f"{self.brand} {self.model} phone is now off"
class Laptop(Device):
  def power_on(self):
    return f"{self.brand} {self.model} phone is now on"
  def power_off(self):
    return f"{self.brand} {self.model} phone is now off"
Device=[Phone("Samsung Galaxy","S24"),Laptop("Dell","HG89")]
for d in Device:
  print(d.power_on(), d.power_off(),"\n")