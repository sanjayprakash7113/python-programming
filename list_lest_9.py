a=[1,2,3,4,5,6]
b=[]
for i in range(len(a)):
    c=1
    for j in range(len(a)):
        if a[i]!=a[j]:
            c=c*a[j]
    b.append(c)
print(b)

a=[5, 2, 6, 1]
b=[]
for i in range(len(a)):
    c=0
    for j in range(i+1,len(a)):
        if a[i]>a[j]:
            c=c+1
    b.append(c)
print(b)
        
a=[4,5,2,10,8]
b=[]
for i in range(len(a)):
    c=False
    for j in range(i+1,len(a)):
        if a[j]>a[i]:
            b.append(a[j])
            c=True
            break
    if not c:
        b.append(-1)
print(b)




a = [1,2,3,2,3,4,5,1]

current = [a[0]]
longest = [a[0]]

for i in range(1, len(a)):
    if a[i] > a[i-1]:
        current.append(a[i])
    else:
        current = [a[i]]

    if len(current) > len(longest):
        longest = current

print(longest)





a = [1, 2, 3, 6, 5]

broken = False

for i in range(len(a) - 1):
    if a[i] > a[i + 1]:
        print(a[i + 1])
        broken = True
        break

if not broken:
    print(None)


a=[1,1,2,2,2,3,3,3,3,1]
c=False
b=[]
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]<=a[j]:
            b.append(a[j])
            c=True
            break
print(b)


    
        
        





















    
