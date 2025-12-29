a= [1, 2, 3, 4]
b=[]
for i in range(len(a)):
    p=1
    for j in range(len(a)):
        if a[i]!=a[j]:
            p=p*a[j]
    b.append(p)
print(b)


a=[1, 2, 3, 2, 4, 3, 5]
b=[]
c=[]
for i in a:
    if i in b:
        if i not in c:
            c.append(i)
    else:
        b.append(i)
print(c)

a=[1,2,3,4,5,6]
b=[]
i=0

while i<len(a):
    if i<len(a):
        b.append(a[i+1])
        b.append(a[i])
        i=i+2
print(b)

a=[1, 2, 3, 4, 5, 6]
b=[]
c=[]
b.append(a[-2])
b.append(a[-1])
for i in a:
    if i not in b:
        b.append(i)
print(b)



a=[3, 1, 4, 2]
b=a[0]
c=a[0]
for i in a:
    if i>b:
        b=i
for j in a:
    if j<c:
        c=j
d=b-c
new_list = []
for i in a:
    new_list.append(d)
print(new_list)

a= [1, 2, 3, 4]
b=0
c=[]
for i in a:
    b=b+i
    c.append(b)
    i=b
print(c)

a=a= [1, 2, 3, 4]
b=0
c=[]
for i in a:
    b=b+i
    c.append(b)
    i=b
print(c)
    
        
    

a=[1,3,5,2]
b=0
c=[]
i=0
for i in range(len(a)-1):
    c.append(a[i+1]-a[i])
c.append(a[-1])
print(c)
    
    
    
    
        
    










        

