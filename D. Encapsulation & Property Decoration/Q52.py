# 52. Implement a `User` class with email validation using setters.
import re
class User:
  def __init__(self,name,email):
    self.name=name
    self.__email=None
    self.email=email

  @property
  def email(self):
    return self.__email
  @email.setter
  def email(self,value):
    pattern=r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern,value):
      self.__email=value
    else:
      print("Invalid email format")

  def display(self):
    print(f"{self.name}, Email: {self.__email}")

u1=User("Muhammad Faizan","bkh@gmail.com")
u1.display()
u1.email="something@gmail.com"
u1.display()