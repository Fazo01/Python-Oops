# 25. Create a class `Shape3D` inherited by `Cube` and `Sphere` with methods for surface area and volume.
import math
class Shape3D:
  def surface_area(self):
    return 0
  def volume(self):
    return 0
class Cube(Shape3D):
  def __init__(self,a):
    self.a=a
  def surface_area(self):
    print("Surface area of cube: ",6*self.a**2)
  def volume(self):
    print("Volume of cube: ",self.a**3)
class Sphere(Shape3D):
  def __init__(self,r):
    self.r=r
  def surface_area(self):
    print("Surface area of sphere: ",4*math.pi*self.r**2)
  def volume(self):
    print("Volume of sphere: ",(4/3)*math.pi*self.r**3)
c=Cube(4)
c.surface_area()
c.volume()
s=Sphere(4)
s.surface_area()
s.volume()