# 51. Write a `Laptop` class with read-only serial number property.
class Laptop:
  def __init__(self,brand,serial_number):
    self.brand=brand
    self.__serial_number=serial_number
  @property
  def serial_number(self):
    return self.__serial_number
  @serial_number.setter
  def serial_number(self,value):
    self.__serial_number=value
  
  def display(self):
    print(F"{self.brand} serial number {self.__serial_number}")
l1=Laptop("Dell","NF12JDLANL1213")
l1.display()
l1.serial_number="BD33KSA233HBD3HK"
l1.display()