a=[1,2,3]
b=[]
for i in a:
    b.append(i)
print(b)

a=[1,2,3,4]
c=0
for i in a:
    c=c+1
print(c)


a=[1,2,34,4]
b=0
for i in a:
    b=b+i
print(b)

a=[1,34,2,3,4,-9]
b=a[0]
for i in a:
    if i<b:
        b=i
print(b)

a=[1,2,3,4,5,6]
c=0
for i in a:
    if i%2==0:
        c=c+1
print(c)




a=[1,2,3,4,5]
b=[]
for i in a:
    if i%2!=0:
        b.append(i)
print(b)


a=[1,2,3,4,5]
b=len(a)
c=0
e=[]
for i in a:
    c=c+i
    d=c//b
for j in a:
    if j>d:
        e.append(j)
print(e)




a=[1,2,3,4,5]
b=[]
for i in a:
    if i%2==0:
        b.append(i*i)
    elif i%2 !=0:
        b.append(i*i*i)
print(b)


a=[1,2,3,4,5,6]
b=[]
for i in a:
    if i not in b:
        b=[i]+b
print(b)


a=[1, 2, 3, 7, 8, 9]
b=10
for i in a:
    for j in a:
        if i+j==b and i!=j:
            print(i,j)


            

a = [1, 2, 3, 2, 4, 3, 4]

for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] == a[j]:
            print(a[i])
            break
    else:
        continue
    break



a=[1,2,3,2,1,4,5]

for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] == a[j]:
            continue
            
        
    else:
        print(a[i])
    break

a = [1, 2, 3, 4]
b = []

for i in a:
    if i % 2 == 0:
        b.append(i * 2)
    else:
        b.append(i * 3)

print(b)


a=[1,2,0,5,7,0,3,0,2,3]
b=[]
c=[]
for i in a:
    if i==0:
        b.append(i)
    else:
        c.append(i)
print(c+b)







a=[1,2,3,4,5,6]
b=[]
for i in a:
    if i<1:
        continue
    c=True
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            c=False
            break
    if c:       
        b.append(i)
print(b)




















