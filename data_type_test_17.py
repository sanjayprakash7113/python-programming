nums=[1,8,6,2,5,4,8,3,7]
mx=0
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        he=min(nums[i],nums[j])
        wit=j-i
        area=he*wit
        mx=max(mx,area)
print(mx)


nums= [100,4,200,1,3,2]
mx=0
l=0
for i in nums:
    if i-1 not in nums:
        cur=i
        l=1
        while cur+1 in nums:
            cur+=1
            l+=1
            mx=max(mx,l)
print(mx)



nums = [0,3,7,2,5,8,4,6,0,1]
n=0
while True:
    if n not in nums:
        print(n)
        break
    else:
        n+=1

nums="abcaabbcb"
c=0

for i in range(len(nums)):
    s=""
    for j in range(i,len(nums)):
        if nums[j] not in s:
            s+=nums[j]
            if len(s)>c:
                c=len(s)
        else:
            break
print(c)



nums = [1,1,1]
k = 2
c=0
for i in range(len(nums)):
    t=0
    for j in range(i,len(nums)):
        t+=nums[j]
        if t==k:
            c+=1
print(c)


nums = [1,1,1,2,2,3]
k = 2
b={}
for i in nums:
    if i in b:
        b[i]+=1
    else:
        b[i]=1
for ke,v in b.items():
    if v>=k:
        print(ke,end=" ")


nums=[1,2,3,4]
res=[]
for i in nums:
    r=1
    for j in nums:
        if i!=j:
            r*=j
    res.append(r)
print(res)
            

















