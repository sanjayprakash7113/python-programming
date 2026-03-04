nums = [-2,1,-3,4,-1,2,1,-5,4]
mx=nums[0]
for i in range(len(nums)):
    t=0
    for j in range(i,len(nums)):
        t+=nums[j]
        mx=max(mx,t)
print(mx)

nums=[[1,3], [2,6], [8,10], [15,18]]
num=[]
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        for a in range(i):
            for b in range(j):
                if a[1]<b[0]:
                    num.append[a[0],b[1]]
                else:
                    num.append[nums[i]]
                    num.append[nums[j]]
print(num)
