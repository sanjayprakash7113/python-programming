class car():
    def drive(self):
        print("start vehicle")
class bike():
    def drive(self):
        print("start")
c=bike()
c.drive()


class num():
    def __init__(self,n):
        self.n=n
    def __add__(self,other):
        return self.n+other.n
c=num(8)
b=num(9)
a=b+c
print(a)


class shape():
    def draw(self):
        print("drawing shape")
class circle(shape):
    def draw(self):
        print("drawing circle")
c=circle()
c.draw()

class a():
    def __init__(self,n):
        self.n=n
    def __add__(self,other):
        return (self.n+other.n)
c=a(10)
b=a(34)
d=c+b
print(d)


class a():
    def __init__(self,n):
        self.n=n
    def add(self,other):
        return (self.n+other.n)
c=a(10)
b=a(34)
d=c+b
print(d)




