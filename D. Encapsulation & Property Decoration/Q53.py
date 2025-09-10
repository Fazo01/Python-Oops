# 53. Create a `Temperature` class with property to set value in Celsius and get in Fahrenheit.
class Temperature:
  def __init__(self,celsius=0):
    self.__celsius=celsius
  @property
  def celsius(self):
    return self.__celsius
  @celsius.setter
  def celsius(self,value):
    self.__celsius=value
  def fahrenheit(self):
    return (self.__celsius*9/5)+32
t1=Temperature(90)

print(t1.celsius)
print(t1.fahrenheit())
t1.celsius=40
print(t1.fahrenheit())