a=[3, 1, 4, 2]
b=[]
for i in range(len(a)):
    c=0
    for j in range(len(a)):
        if a[i]<a[j]:
            c=c+1
    b.append(c)
print(b)
    

        

a=[1,2,3,4]
b=[]
for i in range(len(a)):
    s=0
    for j in range(i+1,len(a)):
        s=s+a[j]
    b.append(s)
print(b)


a = [1, 2, 2, 3, 4, 1, 2, 3]

max_len = 1
curr_len = 1

for i in range(1, len(a)):
    if a[i] > a[i-1]:
        curr_len += 1
        if curr_len > max_len:
            max_len = curr_len
    else:
        curr_len = 1

print(max_len)


a = [1, 2, 3, 4, 5]
b=[]
for i in range(1,len(a)):
    b.append(a[i])
b.append(a[0])
print(b)
    















