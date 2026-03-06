nums = [1,1,1,2,2,3]
k = 2
d={}
for i in nums:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
for ke,v in d.items():
    if v>=k:
        print((ke),end=" ")


d={}
for i in nums:
    d[i]=d.get(i,0)+1
    cur=sorted(d,key=d.get,reverse=True)
print(cur[:2])

nums = [-1,0,1,2,-1,-4]
nums.sort()
a=[]    
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        for k in range(j+1,len(nums)):
            if nums[i]+nums[j]+nums[k]==0:
                triple=[nums[i],nums[j],nums[k]]
                if triple not in a:
                    a.append(triple)
print(a)
            












