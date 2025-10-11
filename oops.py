class emp:
 def __init__(self,n1,n2,n3,n4):
    self.name=n1
    self.age=n2
    self.dept=n3
    self.__salary=n4
    print("start")
 def see(self):
    return self.__salary
 def change(self,n):
    self.__salary=n
 def p_inf(self,location):
    print(self.name,self.age,self.dept,location)
a1=emp("victor",15,"mech",8323)
print(a1.name)


from abc import ABC,abstractmethod
class bike(ABC):
 @abstractmethod
 def cc(self):
    pass
 def seat(self):
    pass
 @abstractmethod
 def wheels(self):
    pass

class tvs(bike):
 def cc(self):
    print("cc")
 def col(self):
   print("col")
 def wheels(self):
   print("wheels")

t1=tvs()
print(t1)
print(t1.cc())
u=t1.wheels()
print(u)
