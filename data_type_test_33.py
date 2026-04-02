nums = [1,1,1]
k=2
l=0
for i in range(len(nums)):
    cur=0
    for j in range(i+1,len(nums)):
       
        while cur<k:
             cur+=nums[j]
        else:
            l+=1
            break
print(l)



nums = [2,7,11,15]
target = 9

d={}
for i in range(len(nums)):
    num=nums[i]
    need=target-num
    if need in d:
        print(d[need],i)
        break
    d[num]=i


nums = [3,2,4]
target = 6
d={}
for i in range(len(nums)):
    num=nums[i]
    need=target-num
    if need in d:
        print(d[need],i)
        break
    d[num]=i




nums = [1,2,3,2,4]
target = 4
d={}
res=set()
for i in range(len(nums)):
    num=nums[i]
    need=target-num
    if need in d:
        pair=tuple(sorted((need,num)))
        res.add(pair)
    d[num]=i
print(list(res))













