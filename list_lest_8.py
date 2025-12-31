a = [3, 1, 4, 2, 3, 5, 1]
b=[]
c=[]
for i in a:
    if i in b:
        if i not in c:
            c.append(i)
    else:
        b.append(i)

print(c)


    
a = [2, 3, 4, 2, 5, 3, 6]
b=[]
for i in range(len(a)):
    c=0
    for j in range(len(a)):
        if a[i]==a[j]:
            c=c+1
    b.append(c)
print(b)




a=[1, 2, 3, 4, 5, 6]
b=[]
for i in range(len(a)):
    c=1
    for j in range(len(a)):
        if a[i]==a[j]:
            continue
        c=1*i
    b.append(c)
print(b)
        
            
