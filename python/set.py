a=[1,2,3,4,5,6,7,8]
b=set(a)
print(b)

print(b.add(676))
print(b)

name={"sanajy","ram","sam"}
print(name.add("victor"))
print(name)
nam={"ece","mech"}
print(name.update(nam))
print(name)

print(name.discard("sriram"))
print(name)
print(name.remove("ram"))
print(name)

a1=input("enter the number").split(",")
a1=list(set(a1))
print(a1)

