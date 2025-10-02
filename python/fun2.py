def cal(a,b):
    
    q=a+b
    y=a-b
    g=a*b
    h=a/b
    print(q,y,g,h, sep='\n')
cal(12,23)

def stu(name,age):
    print("enter the name:",name)
    print("enter the age:",age)
stu("alish",23)

def biodata(name,age,course,profile,poy):
    print("enter the name:",name)
    print("enter the age:",age)
    print("enter the course:",course)
    print("enter the profile:",profile)
    print("enter the poy:",poy)
biodata("victor",20,"mech","engineering student",2025)


def a():
    global x,y
    x=22
    y=33
    print(x,y)
a()


def g4(a,b):
    return a+b
e=g4(2,3)
print(e)


def a(v,c):
    if v>=c:
     return v
    else:
     return c

print(a(90,32))



   




