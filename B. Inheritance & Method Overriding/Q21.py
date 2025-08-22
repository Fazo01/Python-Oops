# 21. Implement a `Publication` class inherited by `Book` and `Magazine`.
class Publication:
  def __init__(self,bookName):
    self.bookName=bookName

  def bookNames(self):
    return self.bookName
  
class Book(Publication):
  def __init__(self, bookName):
    super().__init__(bookName)

  def bookNames(self):
    return self.bookName
  
class Magazine(Publication):

  def __init__(self, bookName):
    super().__init__(bookName)

  def bookNames(self):
    return super().bookName()+1
  
b1=Publication("M")
print(b1.bookNames())
b2=Book("b")
print(b2.bookNames())
b3=Magazine("d")
print(b3.bookName)
