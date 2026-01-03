a = [1,1,2,2,2,3,3,3,3]

longest = []
current = [a[0]]

for i in range(1, len(a)):
    if a[i] == a[i-1]:
        current.append(a[i])
    else:
        if len(current) > len(longest):
            longest = current
        current = [a[i]]

if len(current) > len(longest):
    longest = current

print(longest)


a=[1, 2, 3, 2, 3, 4, 5, 1]
b=[]
c=[a[0]]
for i in range(1,len(a)):
    if a[i]>a[i-1]:
        c.append(a[i])
    else:
        if len(c)>len(b):
            b=c
        c=[a[i]]
if len(b)>len(c):
    print(len(b))
else:
    print(len(c))


a=[5, 3, 4, 2, 1]
b=[]

for i in range(len(a)):
    c=0
    for j in range(len(a)):
        if a[i]<a[j]:
            c=c+1
    b.append(c)
print(b)


a=[3, 1, 4, 2]
b=[]
s=0
for i in a:
    b.append(s)
    s=s+i
print(b)

a=[10,13,15,20]
b=[0]
for i in range(1,len(a)):
    b.append(a[i]-a[i-1])
print(b)

a=[2,4,6,8]
b=[]
s=0
for i in range(len(a)):
    b.append(s)
    s=s+a[i]
print(b)
    
    

a=[5,2,6,1]
d=[]
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]>a[j]:
            d.append(a[j])
            break
d.append(0)
print(d)

a = [5, 2, 6,3]
d = []

for i in range(len(a)):
    c = 0
    for j in range(i+1, len(a)):
        if a[i] > a[j]:
            c += 1
    d.append(c)

print(d)

        















