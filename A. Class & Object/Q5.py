# 5. Write a class `Student` that accepts marks for 3 subjects and calculates the average and grade.
class Student:
  def __init__(self,math,physics,urdu):
    self.math=math
    self.physics=physics
    self.urdu=urdu
  def average(self):
    return (self.math+self.physics+self.urdu)/3
    
  def grade(self):
    avg=self.average()
    if avg>=90 :
      print("A+")
    elif avg>=80 :
      print("A")
    elif avg>=70 :
      print("B")
    elif avg>=60 :
      print("C")
    elif avg>=50 :
      print("D")
    else:
      print("F")
s1=Student(90,90,60)
avg=s1.average()
print("Average:",avg)
s1.grade()