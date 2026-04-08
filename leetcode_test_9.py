nums1 = [1,2,2,1]
nums2 = [2,2]
res=[]
for i in nums1:
    if i in nums2:
        if i not in res:
           res.append(i)
print(res)


jewels = "aA"
stones = "aAAbbbb"
jew=set(jewels)
res=0
for i in stones:
    if i in jew:
        res+=1
print(res)
        
