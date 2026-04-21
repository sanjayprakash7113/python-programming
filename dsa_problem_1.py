nums = [1, 2, 3, 4, 6]
target = 6

left=0
right=len(nums)-1

while left<right:
    s=nums[left]+nums[right]
    if s==target:
        print(left,right)
        break
    elif s>target:
        right-=1
    else:
        left+=1



nums = [1, 1, 2, 2, 3, 4, 4]
left=0

for i in range(1,len(nums)):
    if nums[i]!=nums[left]:
        left+=1
        nums[left]=nums[i]
print(left+1)
print(nums[:left+1])


nums = [0, 1, 0, 3, 12]
left=0
for i in range(len(nums)):
    if nums[i]!=0:
        nums[left]=nums[i]
        left+=1
for i in range(left,len(nums)):
    nums[i]=0
print(nums)


nums = [1,8,6,2,5,4,8,3,7]
left=0
right=len(nums)-1
mx=0
while left<right:
    w=min(nums[left],nums[right])*(right-left)
    mx=max(mx,w)
    if nums[left]<nums[right]:
        left+=1
    else:
        right-=1
print(mx)



nums = [-4, -1, -1, 0, 1, 2]
left=0
right=1
cen=2
for i in range(len(nums)):
    s=nums[left]+nums[right]+nums[cen]
    if s==0:
        print(nums[left],nums[right],nums[cen])
        break
    elif s>0:
        left-=1
        right-=1
        cen-=1
    else:
        left+=1
        right+=1
        cen+=1


















