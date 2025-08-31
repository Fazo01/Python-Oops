# 43. Write a `Book` class where `+` merges authors’ names into one.
class Book:
  def __init__(self,author):
    # self.title=title
    self.author=author
  def __add__(self,other):
    return Book({self.author+other.author})
  def __str__(self):
    return f"author: {self.author}"
b1=Book("Minecraft")
b2=Book("JOK")
print(b1+b2)