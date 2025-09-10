# 57. Write a `Person` class with property for full name (first + last).
class Person:
  def __init__(self,firstName,lastName):
    self.firstName=firstName
    self.lastName=lastName
  @property
  def fullName(self):
    return f"{self.firstName} {self.lastName}"
  @fullName.setter
  def fullName(self,name):
    parts=name.split(" ",1) # split name into two
    if len(parts)==2:
      self.firstName,self.lastName=parts
    else:
      raise ValueError("Full name must include first and last name")

p=Person("Muhammad","Faizan")
print("Full Name: ",p.fullName)