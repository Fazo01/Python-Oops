# 7. Create a class `Book` with title, author, and price attributes. Add a method to display book info.
class Book:
  def __init__(self,title,author,price):
    self.title=title
    self.author=author
    self.price=price
  def ShowInfo(self):
    print(f"Book title: {self.title}")
    print(f"Book author: {self.author}")
    print(f"Book price: {self.price}")
b1=Book("48 Laws of power","Robert Greene",100)
b1.ShowInfo()