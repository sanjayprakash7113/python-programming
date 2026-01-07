t=(1,2,3,4,5,6)
c=0
for i in t:
    if i%2!=0:
        c=c+1
print(c)



b=0
for i in t:
    b=b+i
print(b)


b=t[0]
for i in t:
    if i>b:
        b=i
print(b)


b=0
for i in t:
    if i>10:
        b=b+1
print(b)


t = (5, 3, 5, 2, 3, 1)
a=()
for i in range(len(t)):
    if t[i] not in a:
        a=a+(t[i],)
print(a)

t = (2, 4, 6, 8)
a=()
for i in t:
    a=a+(i*i,)
print(a)



t1 = (1, 2, 3, 4)
t2 = (3, 4, 5, 6)

for i in t2:
    if i not in t1:
        t1=t1+(i,)
print(t1)

t = (1, 2, 2, 3, 3, 3, 4)
a={}
for i in t:
    if i in a:
        a[i]=a[i]+1
    else:
        a[i]=1
print(a)

t = (12, 5, 7, 19, 5, 3)
a=t[0]
b=0
for i in t:
    if i<a:
        b=a
        a=i
print(a)

t = (2, 3, 4, 5, 6, 7, 8, 9, 10)
count = 0

for i in t:
    if i > 1:
        prime = True
        for j in range(2, i):
            if i % j == 0:
                prime = False
                break
        if prime:
            count=count+1

print(count)

t = (12, 7, 9, 4, 15, 8)
a=()
for i in t:
    if i%2!=0:
        a=a+(i,)
b=a[0]
for j in a:
    if j>b:
        b=j
print(b)

















       
