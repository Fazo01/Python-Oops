# 42. Create a `Temperature` class where `>` compares two temperatures.
class Temperature:
  def __init__(self,value,unit="C"):
    self.value=value
    self.unit=unit.upper()
  def to_calsius(self):
    if self.unit=="C":
      return self.value
    elif self.unit=="F":
      return (self.value -32)*5/9
    elif self.unit=="K":
      return self.value-273.15
    else:
      raise ValueError("Unsupported unit")
  def __gt__(self,other):
    return self.to_calsius() > other.to_calsius()
  def __str__(self):
    return f"{self.value}°{self.unit}"
  
t1=Temperature(90,"C")
print(t1)
t2=Temperature(80,"F")
print(t2)
t3=Temperature(80,"K")
print(t3)
print(t1>t2)
