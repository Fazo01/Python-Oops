# 11. Write a class `Counter` that increases count each time an object is created.

class Counter:
  count=0
  def __init__(self):
    Counter.count+=1

  @classmethod
  def counting(cls):
    return cls.count

c1=Counter()
c2=Counter()
c3=Counter()

print(f"Counting: {Counter.counting()}")