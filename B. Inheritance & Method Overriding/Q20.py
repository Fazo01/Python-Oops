# 20. Write a base class `Employee` and subclasses `Manager` and `Developer` with overridden `calculate_salary()` methods.
class Employee:
  def __init__(self,name,base_salary):
    self.name=name
    self.base_salary=base_salary
  def calculate_salary(self):
    return self.base_salary
class Manager(Employee):
  def __init__(self, name, base_salary):
    super().__init__(name, base_salary)
  def calculate_salary(self):
    return super().calculate_salary()+(0.5*self.base_salary)
class Developer(Employee):
  def __init__(self, name, base_salary):
    super().__init__(name,base_salary)
  def calculate_salary(self):
    return super().calculate_salary()+(0.3*self.base_salary)
  
e=Employee("Muhammad",99)
print(f"Employe name: {e.name} \nEmployee salary: {e.calculate_salary()}")
e1=Manager("FS",99)
print(f"Manager salary: {e1.calculate_salary()}")
e2=Developer("FAi",99)
print(f"Developer salary: {e2.calculate_salary()}")