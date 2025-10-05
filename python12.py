s2=[1,2,3,4,5,3,4]
s3=set(s2)
print(s3)

s3.add(34)
print(s3)
s3.pop()
print(s3)
s3.remove(5)
print(s3)
s3.update([45,68,90])
print(s3)

a={1,2,3,4,5,6}
b={3,4,7,8,9}
print(a|b)
print(a-b)
print(a&b)
print(a^b)

w=a.symmetric_difference(b)
print(w)

t=(1,2,3,4,5)
t2=("a",t)

print(t[1:3])

print(t.count(2))
print(t.index(4))
print(t2)
l=list(t)
print(l)




	