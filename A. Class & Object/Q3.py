# 3. Implement a class `Temperature` that stores temperature in Celsius and converts to Fahrenheit.
class Temperature:
  def __init__(self,celsius):
    self.celsius=celsius
  def fahrenheit(self):
    return (self.celsius*9/5)+32
t1=Temperature(2)
print(t1.fahrenheit())