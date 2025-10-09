try:
    a=int(input("enter the value:"))
    b=int(input("enter the value:"))
    c=a/b
    print(c)
except ZeroDivisionError:
    print("b can not be zero")
except ValueError:
    print("enter number only")
finally:
    print("end")

t=lambda f,r,y : f+r+y
print(t(3,4,5))

w=[1,2,3,4]
import math as m
s=[]
for i in w:
    z=lambda i:m.sqrt(i)
    s.append(int(z(i)))
    print(s)


u=list(map(lambda i:m.sqrt(i),w))
print(u)

def s(n):
    return n*n
print(s(5))

pp=[1,2,3]

t=(lambda p:n*n,pp)
print(t)

oo=list(map(int,input("enter the num").split()))
print(oo)

rr=[1,2,3,4,5]
def t(i):
    if i<=3:
        return True
    else:
        return False

g=list(filter(t,rr))
print(g)

uu=list(lambda kk:kk<=2,)
print(uu)


