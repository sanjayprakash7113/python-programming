t = (5, 10, 15, 20, 25)
b=(t[-1],)
c=t[0]
for i in t:
    if i not in b:
        b=b+(i,)
    else:
        b=b+(c,)
print(b)
    
t = (1, 2, 3, 2, 1)
b=()
for i in t:
    b=(i,)+b
    if t==b:
        print(True)
        
t = (1, 2, 3, 4, 5)
l=list(t)
b=5
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]+l[j]==b:
            print((l[i],l[j]))

    
    
