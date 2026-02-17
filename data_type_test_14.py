nums = [100,7,5,6]
ma_x=0

for i in range(len(nums)):
    if (nums[i]+1) in nums:
        ma_x=max((i+1),ma_x)
print(ma_x)
