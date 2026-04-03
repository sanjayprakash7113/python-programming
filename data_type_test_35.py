nums = [0,0,1,1,1,2,2,3,3,4]
left=0

for i in range(1,len(nums)):
    if nums[left]!=nums[i]:
        left+=1
        nums[left]=nums[i]
print(left+1)
