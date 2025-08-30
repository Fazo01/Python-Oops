# 39. Implement a `Cart` class where `+` operator adds items.
class Cart:
  def __init__(self,items):
    self.items=items
  def __add__(self,other):
    return Cart(self.items+self.other)
  def __str__(self):
    return f"Items: {self.items}"
c1=Cart(["Apple","Banana"])
print(c1)