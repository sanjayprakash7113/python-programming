nums = [4, 5, 2, 25]
num=[]
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i]<nums[j] and i<j:
            num.append(nums[j])
            break
if len(nums)!=len(num):
    num.append(-1)
print(num)


