class pfs:
 no_of_student=1022
 def fe(self):
    print("fe")
 def db(self):
    print("sql")


class python(pfs):
 no_of_student=2043
 def fun(self):
    print("def","lambda")
 def oops(self):
    print("class","object")

p1=python()
print(p1.fun())
print(pfs.no_of_student)
print(p1.no_of_student)

print(p1.db())

class company:
 no_of_branch=15
 def mother_company(self):
    print("alphat")
 def owner(self):
    print("share holders")

class google(company):
 no_of_department=150
 def ceo(self):
    print("sunder")
 def location(self):
    print("usa")


class youtube(company):
 no_of_drpartment=20
 def ceo(self):
    print("victor")
 def content(self):
    print("vedio")

t1=youtube()



class grandfa():
 def col1(self):
    print("black")

class son(grandfa):
 def col2(self):
    print("white")
 def age1(self):
    print(50)

class grandson(son):
 def col3(self):
    print("white")
 def  age2(self):
    print(20)

w1=son
print(w1.col2)
t1=grandson
print(t1.col2)
print(t1.col1)
print(t1.col3)



    






 


