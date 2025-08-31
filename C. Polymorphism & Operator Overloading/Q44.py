# 44. Implement a `Counter` class where `+` merges counts of two objects.
class Counter:
  def __init__(self,number):
    self.number=number
  def __add__(self,other):
    return Counter(self.number+other.number)
  def __str__(self):
    return f"Add: {self.number}"
c1=Counter(8)
c2=Counter(9)
print(c1+c2)