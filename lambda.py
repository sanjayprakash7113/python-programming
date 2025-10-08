a=lambda x:x*x
print(a(3))

b=lambda w,e:w+e
print(b(2,3))

d=lambda u:"even" if u%2==0 else "odd"
print(d(8))

p=[1,2,3,4,5]
o=list(map(lambda x:x**2,p))
print(o)

u=list(filter(lambda x:x%3==0,p))
print(u)


from functools import reduce
h=reduce(lambda d,f:d+f,p)
print(h)