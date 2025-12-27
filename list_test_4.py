a=[16, 17, 4, 3, 5, 2]
b=[]
for i in range(len(a)):
    c=-1
    for j in range(i+1,len(a)):
        if a[j]>c:
            c=a[j]
    b.append(c)
print(b)


a=[1, 2, 3, 4, 5]
k=2
n=len(a)
b=[]
for i in range(n-k,n):
    b.append(a[i])
for i in range(n-k):
    b.append(a[i])
print(b)


a=[1, 2, 3, 4, 5]
b=[]
for i in a:
    if i%2==0:
        b.append(i*2)
    elif i%2==1:
        b.append(i*3)
print(b)


a=[1, 2, 3, 4, 5]
b=[]
for i in range(len(a)):
    if i%2==0:
        b.append(a[i]*a[i])
    if i%2 !=0:
        b.append(a[i]*a[i]*a[i])
print(b)


a=[1,2,3,4]
c=[]
for i in range(len(a)):
    b=1
    for j in range(len(a)):
        if a[i]!=a[j]:
            b=b*a[j]
    c.append(b)
print(c)





















            
        





















    
