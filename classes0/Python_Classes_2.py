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


s = Square(int(input()))
s.area()