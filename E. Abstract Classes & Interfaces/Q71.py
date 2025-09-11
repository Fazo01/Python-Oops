# 71. Implement an abstract class `Vehicle` with `start_engine()` and `stop_engine()` methods.
from abc import ABC,abstractmethod
class Vehicle(ABC):
  @abstractmethod
  def start_engine(self):
    pass
  @abstractmethod
  def stop_engine(self):
    pass

class Car:
  def start_engine(self):
    return f"Car engine is started"
  def stop_engine(self):
    return f"Car engine is stop"
class Bike:
  def start_engine(self):
    return f"Bike engine is started"
  def stop_engine(self):
    return f"Bike engine is stop"

Vehicle=[Car(),Bike()]
for v in Vehicle:
  print(v.start_engine())
  print(v.stop_engine())