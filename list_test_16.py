a=[1,2,3,4,5]
t=7
b=0
for i in range(len(a)):
    s=0
    for j in range(i,len(a)):
        s=s+a[j]
        if s<t:
            b+=1
print(b)




a = [1, 2, 3, 4, 5]
t= 6
b=0
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]+a[j]==t:
            b=b+1
print(b)
