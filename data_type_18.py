nums = [1,5,7,1,5,7]
target = 6

seen = set()
pairs = set()
for num in nums:
    complement = target - num
    if complement in seen:
        pair = tuple(sorted((num, complement)))
        pairs.add(pair)
    seen.add(num)
for p in pairs:
    print(p)

nums = [-1,0,1,2,-1,-4]
seen=set()
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        for k in range(j+1,len(nums)):
            if (nums[i]+nums[j]+nums[k])==0:
                triple=tuple(sorted([nums[i],nums[j],nums[k]]))
                seen.add(triple)
for i in seen:
    print(i)


nums = [1,2,3,4]
res=[]
for i in range(len(nums)):
    t=1
    for j in range(len(nums)):
        if nums[i]!=nums[j]:
            t*=nums[j]
    res.append(t)
print(res)


nums = [1,2,3,4,5,6,7]
k = 3
n=len(nums)
k=k%n
print(k)
res=[]
for i in range(n-k,n):
    res.append(nums[i])
for i in range(0,n-k):
    res.append(nums[i])
print(res)
    















