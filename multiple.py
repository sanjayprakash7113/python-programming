class dad:
 def weight(self):
    print("dad class weight")
 def col(self):
    print("dad class col")

class mom:
 def height(self):
    print("mom height")
 def mcol(self):
    print("mom col")

class son(dad,mom):
 def __init__(self,name):
    self.name=name
 def height(self):
    print("son height")
 def weight(self):
    print("son weight")
 def __str__(self):
    return self.name

r1=son("victor")

r1.mcol()



class bike:
 def seat(self):
    print("bike seat")
 def wheel(self):
    print("bike wheeel")

class hero(bike):
 def cc(self):
    print("cc")
 def part(self):
    rint("part")

class honda(bike):
 def engin(self):
    part("engin")
 def col(self):
    part("col")

class hh(hero,honda):
 def milage(self):
    print("km")
 def power(self):
    print("strgngth")

v1=hh()
v1.cc()
v1.seat()
v1.milage()


