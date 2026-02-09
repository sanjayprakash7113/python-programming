a = 256
b = 256
print(a is b)

c = 257
d = 257
print(c is d)

def func(a, L=[]):
    L.append(a)
    return L

print(func(1))
print(func(2))
print(func(3))


d = {}
d[1] = 'a'
d[1.0] = 'b'
d[True] = 'c'
print(d)


gen = (x for x in range(3))
print(list(gen))
print(list(gen))


