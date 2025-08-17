# 16. Create a base class `Shape` with an abstract method `area()`, and subclasses `Square` and `Triangle`.
class Shape:
  def area(self):
    pass
class Squarre(Shape):
  def area(self,side):
    return side**2
class Triangle(Shape):
  def area(self,base,height):
    return 0.5*base*height

s =Squarre()
Squarrearea=s.area(2)
b=Triangle()
Trianglearea=b.area(2,4)
print("SquareArea",Squarrearea)
print("Triangle area",Trianglearea)