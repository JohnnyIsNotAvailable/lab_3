x = int(input())
y = int(input())
class Point():
    def __init__(self, x, y):
        self.x = x 
        self.y = y
        
    def Show(self):
        print(self.x, self.y)
    def Move(self):
        x1 = int(input())
        y1 = int(input())
        self.x = x1 
        self.y = y1
    def Dist(self):
        dist = abs(x - y)
        print(dist)
        
pl = Point(x,y)
pl.Dist()
pl.Show()
pl.Move() 