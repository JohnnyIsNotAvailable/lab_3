class Shape:
    area = 0
    def __init__(self):
        pass

class Square(Shape):

    def __init__(self, length):
        self.length = length

    def area(self):
        a = (self.length * self.length)
        print(a)

class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        a = (self.length * self.width)
        print(a)

s = Rectangle(int(input()), int(input()))
s.area()

