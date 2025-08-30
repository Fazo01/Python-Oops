# 31. Implement operator overloading for a `Vector` class to support `+` and `-`.
class Vector:
  def __init__(self,x,y):
    self.x=x
    self.y=y
  def __add__(self,other):
    return Vector(self.x+other.x,self.y+other.y)
  def __sub__(self,other):
    return Vector(self.x-other.x,self.y-other.y)
  def __repr__(self):
    return f"Vector ({self.x},{self.y})"
v1=Vector(1,3)
v2=Vector(2,1)
print(v1+v2)
print(v1-v2)