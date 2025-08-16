# 6. Implement a class `Circle` with a radius attribute and methods to calculate area and circumference.
import math
class Circle:
  def __init__(self,radius):
    self.radius=radius
  def area(self):
    return math.pi*(self.radius**2)
  def circumference(self):
    return 2*math.pi*self.radius
c1=Circle(3)
print(f"Area of a circle: {c1.area()}")
print(f"Circumferance of circle: {c1.circumference()}")