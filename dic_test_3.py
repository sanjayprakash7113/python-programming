a = [1, 3, 2, 1, 4, 1, 3, 3, 3]
b={}
for i in a:
    if i in b:
        b[i]=b[i]+1
    else:
        b[i]=1
val=0
key=0
for j in b:
    if b[j]>val:
        val=b[j]
        key=j
print(key)


a = [4, 5, 1, 2, 1, 5, 3]
b={}
for i in a:
    if i in b:
        b[i]=b[i]+1
    else:
        b[i]=1
val=1
key=0
for j in b:
    if b[j]==val:
        val=b[j]
        key=j
        break
print(key)



a = [1, 2, 3, 4, 5, 6]
b={}
for i in a:
    if i%2==0:
        if x not in b:
            b[i]=[]
            b["even"].append(i)
    else:
        b[i]=[]
        b["odd"].append(i)
print(b)















    
