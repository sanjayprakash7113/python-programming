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


nums = [1,2,3,4,5,6]
k = 3

su_m=sum(nums[:k])
ma_x=su_m
for i in range(k,len(nums)):
    su_m+=nums[i]
    su_m-=nums[i-k]
    ma_x=max(su_m,ma_x)
print(ma_x)



s = "abcabcbb"
mx=0
for i in range(len(s)):
    cur=""
    for j in range(i,len(s)):
        if s[j] not in cur:
            cur+=s[j]
            mx=max(mx,len(cur))
        else:
            break

print(mx)


seen=set()
left=0
mx=0
for i in range(len(s)):
    while s[i] in seen:
        seen.remove(s[left])
        left+=1
    seen.add(s[i])
    mx=max(mx,i-left+1)
print(mx)

nums = [4, 2, 1, 7, 8, 1, 2, 8]
k = 8
mx=0
for i in range(len(nums)):
    cur=0
    l=0
    for j in range(i+1,len(nums)):
        if cur<k:
            cur+=nums[j]
            l+=1
            mx=max(mx,l)
print(mx)
        



      

