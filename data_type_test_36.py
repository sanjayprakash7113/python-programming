nums = [2,1,5,1,3,2]
k = 3


nums = [1,4,2,10,2,3,1,0,20]
k = 4

sm=sum(nums[:k])
mx=sm
for i in range(k,len(nums)):
    sm+=nums[i]
    sm-=nums[i-k]
    mx=max(mx,sm)
print(mx)


nums = [1,12,-5,-6,50,3]
k = 4
sm=sum(nums[:k])
mx=sm/k
for i in range(k,len(nums)):
    sm+=nums[i]
    sm-=nums[i-k]
    avg=sm/k
    mx=max(mx,avg)
print(mx)



s = "abcabcdbb"
left=0
res=set()
mx=0
for i in range(len(s)):
    while s[i] in res:
        res.remove(s[left])
        left+=1
    res.add(s[i])
    mx=max(mx,i-left+1)
print(mx)
