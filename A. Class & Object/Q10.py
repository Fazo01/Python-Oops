# 10. Create a class `Person` with methods to update name and age, ensuring age is a positive integer.
class Person:
  def __init__(self,age,name):
    
    self.name=name
    if age>0:
      self.age=age
    else:
      print("Age should be in positive")

  def ShowDetials(self):
    print(f"Name: {self.name} and Age: {self.age}")

  def update_name(self,new_name):
     self.name=new_name
  
  def update_age(self,new_age):
    if new_age>0:
      self.age=new_age
    else:
      print("Age should be in positive")
p1=Person(9,"Muhammad Faizan")
p1.ShowDetials()
p1.update_name("Ahmad")
p1.update_age(10)
p1.ShowDetials()
