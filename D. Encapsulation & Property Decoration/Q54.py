# 54. Write a `Rectangle` class with private width and height, and computed area property.
class Rectangle:
  def __init__(self,width,height):
    self.__width=width
    self.__height=height
  @property
  def width(self):
    return self.__width
  @width.setter
  def width(self,value):
    if value>0:
      self.__width=value
    else:
      print("Insufficient value")
  
  @property
  def height(self):
    return self.__height
  def height(self,value):
    if value>0:
      self.__height=value
    else:
      print("Insufficient value")
  def area(self):
    return self.__width*self.__height
r1=Rectangle(5,10)
print(r1.area())