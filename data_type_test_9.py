nums = [100, 4, 200, 1, 3, 2]
nums.sort()
max_l=0
for i in nums:
    if (i+1) in nums:
        max_l=max(max_l,i+1)
print(max_l)


s=set(nums)
lo=0

for i in s:
    if i-1 not in s:
        c=i
        l=1
        while c+1 in s:
            c+=1
            l+=1
        lo=max(lo,l)
print(lo)

nums = [1, 2, 3, 4, 5, 6, 7]
k = 3

k=k%len(nums)
res=nums[-k:]+nums[:-k]

print(res)

nums = [3, 4, 5, 2]
b=0
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        res=nums[i]*nums[j]
        if res>b:
            b=res
print(b)
        
