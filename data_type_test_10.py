nums = [2, 0, 1]
nums.sort()
i=0
for j in nums:
    if i==j:
        i+=1
    else:
        print(i)
print(i)
    
nums = [0,1,0,3,12]
a=0
for i in range(len(nums)):
    if nums[i]!=0:
        nums[a]=nums[i]
        a+=1
for j in range(a,len(nums)):
    nums[j]=0
print(nums)


nums = [2, 3, 10, 6, 4, 8, 1]
b=0
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
            res=nums[j]-nums[i]
            if res>b:
                b=res
print(b)


nums = [1,2,2,3]
inc=True
dec=True
for i in range(1,len(nums)):
    if nums[i]<nums[i-1]:
        inc=False
    if nums[i]>nums[i-1]:
        dec=False
print(inc or dec)
