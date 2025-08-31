# 45. Create a `ListWrapper` class to concatenate lists using `+`.
class ListWrapper:
  def __init__(self,data=None):
    if data is None:
      data=[]
    self.data=data
  def __add__(self,other):
    return ListWrapper(self.data+other.data)
  def __str__(self):
    return f"Data= {self.data}"
l=ListWrapper([1,2,3])
l2=ListWrapper([4,5,6])
print(l+l2)