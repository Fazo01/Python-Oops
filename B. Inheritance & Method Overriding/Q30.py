# 30. Implement a `Shape` class inherited by `Rectangle` and `Circle` with overridden `perimeter()` methods.
import math
class Shape:
  def __init__(self,name):
    self.name=name
  def perimeter(self):
    print(self.name)

class Rectangle(Shape):
  def __init__(self,length,width):
    self.length=length
    self.width=width
  def perimeter(self):
    print("Perimeter of Rectangle: ",2*(self.length+self.width))

class Circle(Shape):
  def __init__(self,radius):
    self.radius=radius
  def perimeter(self):
    print("Perimeter of Circle: ",2*math.pi*self.radius)

s=Shape("Rectangle , Circle")
s.perimeter()
r=Rectangle(2,4)
r.perimeter()
c=Circle(9)
c.perimeter()