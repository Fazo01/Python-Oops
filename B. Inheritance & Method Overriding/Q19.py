# 19. Create a class `Person` inherited by `Teacher` and `Student`, each with additional attributes.
class Person:
  def __init__(self,character):
    self.character=character

class Teacher(Person):

  def __init__(self,character,name):
    super().__init__(character)
    self.name=name

  def entity(self):
    print(f"Character of a person: {self.character} \n.Character Name:{self.name}")

class Student(Person):
  def __init__(self,character,name,Rollno):

    super().__init__(character)
    self.name=name
    self.Rollno=Rollno

  def entity(self):
    print(f"Character of a person: {self.character} \n.Character Name:{self.name} \n.Character Name:{self.Rollno}")

p1=Teacher("bad","Muhammad Faizan")
p2=Student("Good","Muhammd Faizan","9090")

p1.entity()
p2.entity()