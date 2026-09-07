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


if __name__ == '__main__':
    r = Rectangle(4, 5)
    print(r.area())
    print(r.perimeter())