s = "cat dog cat mouse dog cat"
s=s.split()
b={}
for i in s:
    if i in b:
        b[i]+=1
    else:
        b[i]=1
c=0
ans=None
for k,v in b.items():
    if v>c:
        c=v
        ans=k
print(ans)


nums = [1, 2, 3, 4, 5]
c=0
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if i<j and (nums[i]+nums[j])%2==0:
            c+=1
print(c)

nums = [1, 2, 2, 3, 4, 5, 5]
num=[]
for i in nums:
    if i not in num:
        num.append(i)   
target = 6
c=[]
for i in range(len(num)):
    for j in range(i,len(num)):
        if (num[i]+num[j])==target:
            c.append((num[i],num[j]))
print(c)




nums = [1, 2, 2, 3, 4, 5, 5]
target=6
nums.sort()
b=[]
left=0
right=len(nums)-1
while left<=right:
    s=nums[left]+nums[right]
    if s==target:
        b.append((nums[left],nums[right]))
        while left<right  and nums[left]==nums[left+1]:
            left+=1
        while left<right and nums[right]==nums[right-1]:
            right-=1
        left+=1
        right-=1
    elif s<target:
        left+=1
    else:
        right-=1
print(b)










