#tuples are immutable but inner items can imtate
t=(10,[4,3,2],89,8)
t[1].append(89)
print(t)

#packing
t1 = (1,2,3)
print(t1)
#unpacking
a,d,c=(6,4,3)
print(d)
#extra
(a,*b,c)=(1,2,3,4,5,6,90,4,3)
print(b)
print(a,c)

#tuple as a dictionary key
a={(1,2):[3,2,4,3]}
print((1,2))

#tuple nestted trick
t=((4,1),(5),(6),9,(3,[5,3,2]),[7])
t[4][1].append(0)
print(t)
t[5].append(89)
print(t)

#concatination and repetation
t1=(1,2,3)
t2=(5,6,7)
print(t1 + t2)
u=t1*2
print(u*2)
