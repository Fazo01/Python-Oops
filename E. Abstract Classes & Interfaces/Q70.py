# 70. Create an abstract class `Game` with `start()` and `end()` methods.
from abc import ABC,abstractmethod

class Game(ABC):
  @abstractmethod
  def start(self):
    pass
  @abstractmethod
  def end(self):
    pass
class Cricket(Game):
  def start(self):
    return "Cricket game is started"
  def end(self):
    return "Cricket game is end"
class football(Game):
  def start(self):
    return "football game is started"
  def end(self):
    return "football game is end"
  
Game=[Cricket(),football()]
for g in Game:
  print(g.start())
  print(g.end())