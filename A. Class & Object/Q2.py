# 2. Write a class `Rectangle` that calculates area and perimeter. Add a method to compare two rectangles by area.
class Rectangle:
  def __init__(self,length,width):
    self.length=length
    self.width=width

  def area(self):
    return self.length*self.width
  
  def perimeter(self):
    return 2*(self.length+self.width)
  
  def Compare(self,other):
    if self.area()>other.area():
      print("Other is smaller")
    elif other.area()>self.area():
      print("Other is bigger")
    else:
      print("Both are similar")


rec1=Rectangle(1000,1000)
rec2=Rectangle(1000,9000)
print(rec1.area())
print(rec2.area())
print(rec1.Compare(rec2))