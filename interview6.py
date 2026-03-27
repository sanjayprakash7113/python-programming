nums = [3, 5, 1, 8, 2]
mx=nums[0]
for i in nums:
    if i>mx:
        mx=i
print(mx)

for i in nums:
    if i<mx:
        mx=i
print(mx)

nums.sort()
print(nums[0],nums[-1])


nums = [10,47, 20, 4, 45, 99]
s=0
mx=0
for i in nums:
    if i>mx:
        s=mx
        mx=i
    elif i>s and i!=mx:
        s=i
print(s)


nums = [1, 2, 2, 3, 4, 4, 5]
org=[]
for i in nums:
    if i not in org:
        org.append(i)
print(org)


nums = [1, 2, 3, 4, 5]
rev=""
for i in str(nums):
    rev=i+rev
print(rev)




nums = [0, 1, 0, 3, 12]
left=0
for i in range(len(nums)):
    if nums[i]!=0:
        nums[left]=nums[i]
        left+=1
for i in range(left,len(nums)):
    nums[i]=0
print(nums)












