nums = [3,2,3]
d={}
a=len(nums)/2
for i in nums:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
for k,v in d.items():
    if v>a:
        print(k)

for i in range(len(nums)):
    if nums.count(nums[i])>a:
        print(nums[i])
        break
    
nums = [2,7,11,15]
target = 9

for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        sub=(nums[i]+nums[j])
        if sub==target:
            print((i,j))
            break



nums = [1,5,3,4,2]
k = 2

nums = [8,12,16,4,0,20]
k = 4
n=0

for i in nums:
    for j in nums:
        if (j-i)==k:
            n+=1
print(n)


nums = [2,3,-2,4]
mx=nums[0]
for i in range(len(nums)):
    sub=1
    for j in range(i,len(nums)):
            sub*=nums[j]
            mx=max(mx,sub)
print(mx)



nums = [2,3,-2,4]

mx = nums[0]

for i in range(len(nums)):
    sub = 1
    for j in range(i, len(nums)):
        sub *= nums[j]
        mx = max(mx, sub)

print(mx)














