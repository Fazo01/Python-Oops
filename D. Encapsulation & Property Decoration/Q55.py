# 55. Implement a `Movie` class with a property to check if it’s a blockbuster based on rating.
class Movie:
  def __init__(self,title,rating):
    self.title=title
    self.rating=rating
  @property
  def is_blockbluster(self):
    return self.rating>=8.0
m1=Movie("Minecraft",5.6)
print(m1.title, "Blockbuster?" ,m1.is_blockbluster)