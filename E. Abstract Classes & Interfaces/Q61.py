# 61. Create an abstract class `Shape` with methods `area()` and `perimeter()`.
from abc import ABC,abstractmethod
class Shape(ABC):
  @abstractmethod
  def area(self):
    pass
  @abstractmethod
  def parimeter(self):
    pass
  
class Rectangle(Shape):
  def __init__(self,width,length):
    self.width=width
    self.length=length
  def area(self):
    return self.width*self.length
  def parimeter(self):
    return 2*(self.length+self.width)

class square(Shape):
  def __init__(self,side):
    self.side=side

  def area(self):
    return self.side**2

  def parimeter(self):
    return 4*self.side

Shape=[Rectangle(4,5),square(6)]
for s in Shape:
  print(f"{s.__class__.__name__} => Area: {s.area()}, Parimeter: {s.parimeter()}")