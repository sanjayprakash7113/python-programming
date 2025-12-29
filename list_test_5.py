a= [1, 2, 3]
b=[]
for i in a:
    b.append(2*i)
print(b)
            
a= [1, 2, 3, 4, 5]
b=[]
for i in a:
    if i%2==0:
        continue
    b.append(i)
print(b)

a= [1, 4, 2, 5, 3, 6]
b=0
for i in a:
    if i>3:
        b+=1
print(b)

a= [3, 1, 9, 2, 7]
b=a[0]
for i in a:
    if i>b:
        b=i
print(b)

a=[1, 2, 3, 4, 5]
b=[]
for i in a:
    if i%2==0:
        b.append(i*i)
print(b)


a=[1,2,3,4,5]
b=0
for i in a:
    b+=i
c=b//len(a)
d=[]
for j in range (len(a)):
    if a[j]>c:
        d.append(a[j])
print(d)
   

a= [3,8, 1, 10, 2, 7,9]
b=0
c=0
for i in a:
    if i>b:
        c=b
        b=i
    elif c<i and c!=b:
        c=i
print(c)























    
        
