# 34. Implement a `Matrix` class that supports matrix addition.
class Matrix:
  def __init__(self,data):
    self.data=data
    self.row=len(data)
    self.col=len(data[0])
  def __add__(self,other):
    if self.row!=other.row or self.col!=other.col:
      raise ValueError("Matrix dimension must match for addition")
    result=[[self.data[i][j]+other.data[i][j] for j in range(self.col)]
             for i in range(self.row)]
    return Matrix(result)
  def __str__(self):
    return "\n".join([" ".join(map(str,row)) for row in self.data])
m1=Matrix([[1,2,3],[4,5,6]])
m2=Matrix([[7,8,9],[10,11,12]])
print(m1)
print(m2)
print(m1+m2)