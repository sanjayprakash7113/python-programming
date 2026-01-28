a=[1,2,3,4,5,6,7]
target=8
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]+a[j]==target and i<j:
            ans=((a[i],a[j]))
            break
print(ans)



left=0
right=len(a)-1
ans=None

while left<right:
    s=(a[left]+a[right])

    if s==target:
        ans=((a[left],a[right]))
        left+=1
        right-=1
    elif s<target:
        left+=1
    else:
        right-=1
print(ans)




a = [1, 2, 3, 4, 5]
target = 7
c=0
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if (a[i]+a[j])<target:
            c+=1
print(c)



left=0
right=len(a)-1
c=0
while left<right:
    if a[left]+a[right]<target:
        c+=(right-left)
        left+=1
    else:
        right-=1
print(c)
    
