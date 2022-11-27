import math
class circle:
    def __init__(self, r):
        self.r = r
    def radius(self):
        return self.r
    def diametr(self):
        return self.r*2
    def __len__(self):
        return 2 * math.pi * self.r
    def pl(self):
        return math.pi * self.r**2
    def nr(self):
        return self.r * n
    def __mul__(self, other):
        return circle((2 * math.pi * self.r)*(2 * math.pi *(other.r * self.r)))
r = int(input())
n = int(input())
z = circle(r)*circle(n)
obj = circle(r)
print(obj.radius(), obj.diametr(), obj.__len__(), obj.pl(), obj.nr(), z.r, sep='\n')


class circle1(circle):
    def __init__(self, x, y):
        self.x=x
        self.y=y
    def center(self):
        return self.x, self.y
    def pr(self):
        x=self.x + X
        y=self.y + Y
        return x, y
    def d(self):
        return ((self.x + X)*2 + (self.y + Y)*2) ** 0.5
x, y = map(int, input().split())
X, Y = map(int, input().split())
obj=circle1(x, y)
print(obj.center(), obj.pr(), obj.d(), sep='\n')
