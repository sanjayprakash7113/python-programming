a=(1, 2, 3)
b=list(a)
print(b)

a=[1,2,3,4,5]
b=0
for i in a:
    b=b+i
print(b)
c=b//len(a)
d=[]
for j in a:
    if c<j:
        d.append(j)
print(d)

a=[1, 2, 3, 4, 5, 6]
b=[]
c=[]
for i in a:
    if i%2==0:
        b.append(i)
    elif i%2==1:
        c.append(i)
print(b+c)
    
