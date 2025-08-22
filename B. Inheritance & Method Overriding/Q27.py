# 27. Implement a class `Employee` with a `display()` method, overridden by `Manager` to show more details.
class Employee:
  def __init__(self,name,salary):
    self.name=name
    self.salary=salary
  def display(self):
    print(f"Employee name: {self.name}\nSalary: {self.salary}")
class Manager(Employee):
  def __init__(self, name, salary,department):
    super().__init__(name, salary)
    self.department=department
  def display(self):
    super().display()
    print(f"Department {self.department}")
  
m=Manager("Muhammad Faizan",9000,"BSSE")
m.display()