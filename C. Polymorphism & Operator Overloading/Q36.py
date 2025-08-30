# 36. Implement `__str__` and `__repr__` for a `Person` class for better printing.
class Person:
  def __init__(self,title,author):
    self.title=title
    self.author=author
  def __str__(self):#Goal: return a readable / user-friendly string
    return f"{self.title} and author {self.author}"
  def __repr__(self):#Goal: return a developer-friendly string that ideally could recreate the object
    return f"Title={self.title} and author={self.author}"
p1=Person("My life","Muhammad Faizan")
print(p1)
print(repr(p1))