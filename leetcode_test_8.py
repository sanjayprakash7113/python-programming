height = [1,8,6,2,5,4,8,3,7]
left=0
right=len(height)-1
mx=0
for i in range(len(height)):
    while left<right:
        pair=(min(height[left],height[right]))*(right-left)
        mx=max(mx,pair)
        if height[left]<height[right]:
            left+=1
        else:
            right-=1
print(mx)
        
nums = [-1,0,1,2,-1,-4]
res=set()
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        for k in range(j+1,len(nums)):
            if nums[i]+nums[j]+nums[k]==0:
                pair=tuple(sorted([nums[i],nums[j],nums[k]]))
                res.add(pair)
print(list(res))


nums = [1,1]

s = set(nums)
res = []

for i in range(1, len(nums)+1):
    if i not in s:
        res.append(i)

print(res)
        
