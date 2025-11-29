num=[1,1,2,3,3]
b=[]
for i in num:
    if i not in b:
        b.append(i)
print(b)
for i in num:
    for j in b:
        if i==j:
            continue
        print(i)
