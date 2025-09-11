# 64. Create an abstract class `Appliance` with methods `turn_on()` and `turn_off()`.
from abc import ABC,abstractmethod
class Appliance(ABC):
  @abstractmethod
  def turn_on(self):
    pass
  @abstractmethod
  def turn_off(self):
    pass
class Fan(Appliance):
  def turn_on(self):
    return "fan is on"
  def turn_off(self):
    return "fan is off"
class Light(Appliance):
  def turn_on(self):
    return "fan is on"
  def turn_off(self):
    return "fan is off"
Appliance=[Fan(),Light()]
for a in Appliance:
  print(a.turn_on())
  print(a.turn_off())