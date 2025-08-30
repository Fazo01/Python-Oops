# Create a `Time` class that supports adding two time objects using `+` operator.
class Time:
  def __init__(self,hours,minutes,seconds):
    self.hours=hours
    self.minutes=minutes
    self.seconds=seconds
  def __add__(self,other):
    total_seconds=self.seconds+other.seconds
    total_minutes=self.minutes+other.minutes+(total_seconds//60)
    total_hours=self.hours+other.hours+(total_seconds//60)

    seconds=total_seconds%60
    minutes=total_minutes%60
    hours=total_hours
    return Time(hours,minutes,seconds)
  def __str__(self):
    return f"Missed Time: {self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"
t1=Time(12,5,23)
t2=Time(3,5,1)
print(t1+t2)