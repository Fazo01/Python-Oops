# 9. Implement a class `Employee` with methods to set and get salary, ensuring salary can’t be negative.
class Employee:
  def __init__(self, setsalary):
    self.setsalary=setsalary
  def getsalary(self):
    if(self.setsalary<=0):
      print("salary should be in positive")
    else:
       print(f"Your salary: {self.setsalary}")
s1=Employee(90)
s1.getsalary()