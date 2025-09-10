# 48. Write a `Student` class with private marks and property to calculate grade.
class Student:
  def __init__(self,name,marks):
    self.name=name
    self.__marks=marks

  @property
  def marks(self):
    return self.__marks
  
  @marks.setter
  def marks(self,value):
    if 0<=value<=100:
      self.__marks=value
    else:
      print("Marks should be in positive")

  # @property
  def grade(self):
    if self.__marks>=90:
      return f"Name: {self.name} Grade: +A"
    elif self.__marks>=80:
      return f"Name: {self.name} Grade: A"
    elif self.__marks>=70:
      return f"Name: {self.name} Grade: B"
    elif self.__marks>=60:
      return f"Name: {self.name} Grade: C"
    elif self.__marks>=50:
      return f"Name: {self.name} Grade: D"
    else:
      return f"Name: {self.name} Grade: F"
s1=Student("Muhammad Faizan",90)
print(s1.grade())