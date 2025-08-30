# 33. Write a `Distance` class to add and compare distances in meters.
class Distance:
  def __init__(self,meters):
    self.meters=meters
  def __add__(self,other):
    return Distance(self.meters+other.meters)
  def __eq__(self, other):
    return self.meters==other.meters
  def __lt__(self,other):
    return self.meters<other.meters
  def __gt__(self,other):
    return self.meters>other.meters
  def __repr__(self):
    return f"{self.meters} meters"

d1=Distance(99)
d2=Distance(8)
print(d1+d2)
print(d1==d2)
print(d1>d2)
print(d1<d2)