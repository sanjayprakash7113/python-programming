s = "aaabbcc"
mx=0
cur=1
for i in range(1,len(s)):
    if s[i]==s[i-1]:
        cur+=1
    else:
        cur=1
    mx=max(mx,cur)
print(mx)






nums=[1,2,3]
k=3
mx=0
l=0
cur=0
for i in range(len(nums)):
    if nums[i]==k or cur==k:
        l+=1
    else:
        cur+=nums[i]
    mx=max(mx,l)
print(mx)
