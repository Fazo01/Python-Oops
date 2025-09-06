# Implement a `Point` class that supports distance calculation using `-` operator.
import math
class Point:
  def __init__(self,x,y):
    self.x=x
    self.y=y
  def __sub__(self,other):
    return math.sqrt((self.x-other.x)**2+(self.y-other.y)**2)
  def __str__(self):
    return f"Matrix: ({self.x}, {self.y})"
p1=Point(1,3)
p2=Point(3,4)
print(p1-p2)