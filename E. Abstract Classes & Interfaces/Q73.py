# 73. Create an abstract class `Shape3D` with methods for `volume()` and `surface_area()`.
from abc import ABC, abstractmethod
import math

# Abstract Class
class Shape3D(ABC):
    @abstractmethod
    def volume(self):
        pass

    @abstractmethod
    def surface_area(self):
        pass

class Cube(Shape3D):
    def __init__(self, side):
        self.side = side

    def volume(self):
        return self.side ** 3

    def surface_area(self):
        return 6 * (self.side ** 2)
c=Cube(5)
print(c.volume())

print(c.surface_area())