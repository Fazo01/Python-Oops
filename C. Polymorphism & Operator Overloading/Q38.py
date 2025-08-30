# 38. Create a `Score` class to compare scores using `>` and `<` operators.
class Score:
  def __init__(self,scoreNo):
    self.scoreNo=scoreNo
  def __lt__(self,other):
    return self.scoreNo<other.scoreNo
  def __gt__(self,other):
    return self.scoreNo>other.scoreNo
  def __repr__(self):
    return f"Score:{self.scoreNo}"
s1=Score(1)
s2=Score(3)
print(s1>s2)
print(s1<s2)