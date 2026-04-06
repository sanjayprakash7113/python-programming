nums = [1,2,1,1,7]
target = 7
left=0
mx=float('inf')
cur=0

for i  in range(len(nums)):
    cur+=nums[i]
    while cur>=target:
        mx=min(mx,i-left+1)
        cur-=nums[left]
        left+=1
        
print(mx)


nums = [1,2,1,0,1,1,0]
k = 4

left=0
cur=0
mx=0
for i in range(len(nums)):
    cur+=nums[i]
    while cur>k:
        mx=max(mx,i-left+1)
        cur-=nums[left]
        left+=1
print(mx)


s = "eceba"
k = 2
left=0
mx=0

for i in range(len(s)):
    res=set()
    for j in range(i,len(s)):
        res.add(s[j])
        if len(res)<=k:
            mx=max(mx,j-i+1)
        else:
            break
print(mx)




