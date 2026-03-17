nums = [[1,3], [2,6], [8,10], [15,18]]
nums.sort()
res=[nums[0]]

for st,en in nums[1:]:
    last=res[-1][1]
    if st<=last:
        res[-1][1]=max(last,en)
    else:
        res.append([st,en])
print(res)



nums=[100,2,3,4]
k=3
k=k%len(nums)
res=nums[-k:]+nums[:-k]
print(res)

nums=[2,3,2,3,5]
for i in range(len(nums)):
    if nums.count(nums[i])==1:
        print(nums[i])
        break
