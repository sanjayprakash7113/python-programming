nums = [5,6,7,8]
dic={}
for i in nums:
    if i in dic:
        print(True)
        break
    dic[i]=1
else:
    print(False)


nums=[3,2,4]
t=6
d={}
for i in range(len(nums)):
    num=nums[i]
    need=t-num
    if need in d:
        print(d[need],i)
        break
    d[num]=i



        
s = "aabbcde"
d={}
for i in s:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
for i in s:
    if d[i]==1:
        print(i)
        break

nums1 = [1,2,2,1]
nums2 = [2,2]
d={}
for i in nums1:
        if i in d:
            d[i]+=1
        d[i]=1
for j in nums2:
    if j in d:
        print(j)
        break

num= [100,4,200,1,3,2]
nums=set(num)
mx=0
for i in nums:
    l=0
    if i-1 not in nums:
        cur=i
        l=1
        while cur+1 in nums:
            cur+=1
            l+=1
            mx=max(mx,l)
print(mx)
            

nums = [1,2,3,4,6]
target = 6
left=0
right=len(nums)-1
while left<right:
    if (nums[left]+nums[right])==target:
        print(left,right)
        break
    else:
        left+=1
        right-=1


















            
            




    
