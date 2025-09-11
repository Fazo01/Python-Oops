# 63. Write an abstract class `Transport` with subclasses `Bus` and `Train`.
from abc import ABC,abstractmethod
class Transport(ABC):
  
  def __init__(self,capacity,speed):
    self.capacity=capacity
    self.speed=speed
  @abstractmethod
  def move(self):
    pass

class Bus(Transport):
  def move(self):
    return f"Bus carrying {self.capacity} passenger moves at {self.speed} km/h on road"
class Train(Transport):
  def move(self):
    return f"Train carrying {self.capacity} passenger moves at {self.speed} km/h on road"
  
Transport=[Bus(100,56),Train(300,400)]
for t in Transport:
  print(t.move())