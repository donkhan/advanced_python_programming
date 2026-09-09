import math
from abc import ABC, abstractmethod


class Shape:
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, l, b):
        self.l = l
        self.b = b

    def area(self):
        return self.l * self.b

    def perimeter(self):
        return 2 * (self.l + self.b)


class Triangle(Shape):
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        s = (a + b + c) / 2
        return math.sqrt(s * (s-a) * (s-b) * (s-c))



if __name__ == '__main__':
    r = Rectangle(4, 5)
    print(r.area())
    print(r.perimeter())