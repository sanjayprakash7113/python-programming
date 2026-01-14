a=[2,1,5,1,3,2]
b=3
c=0
for i in range(len(a)-b+1):
    x=a[i]+a[i+1]+a[i+2]
    if x>c:
        c=x
print(c)

a=[1,1,1]
t=2
b=0
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]+a[j]==t:
            b=b+1
print(b)

