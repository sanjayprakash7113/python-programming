#frozenset --immudable caN not add or remove element 
f=frozenset([1,2,3,4,5])
print(f)

#s = { {1,2}, {3,4} }   # ❌ error

s = { frozenset({1,2}), frozenset({3,4}) }
print(s)

s = {frozenset([1, 2]), frozenset([3, 4])}
print(s)  # {frozenset({1, 2}), frozenset({3, 4})}

s={f,5,3}
print(s)

 #s={(2,3,[5,6])}
# print(s)--type error

s={3,(3,4,5)}
print(s)

#comperhension
s={1,2,3,4,5}
u={s*s for s in range(5)}
print(u)

u={s for s in range(5) if s%2==0}
print(u)


#mudation set during the itration
s={1,2,3,4}
for i in s.copy():
    if i%2==0:
        s.remove(i)
        print(s)
d=[i for i in s if i%2==0]

for i in d:
    s.remove(i)
print(s)
    


#issubset()
a={1,2,3,4}
b=[1,2,3,4,5]
print(a.issubset(b))
# print(b.issubset(a))--error

a={1,2,3}
b={1,2,3,4}
print(b.issubset(a))

#issuperset()
a={1,2,3,4}
b=[1,2,3,4,5]
print(a.issuperset(b))

a={1,2,3,4}
b={1,2,3}
print(a.issuperset(b))
print(b.issuperset(a))

#isdisjoint
A = {1, 2}
B = {3, 4}
print(A.isdisjoint(B))  # True

A = {1, 2}
B = [2, 5, 6]
print(A.isdisjoint(B))  # False (2 is common)

a={1,2,3,4}
b={5,6,7,8}
print(a.isdisjoint(b))
print(b.isdisjoint(a))














