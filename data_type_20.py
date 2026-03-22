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
l=0
for i in range(len(nums)):
    cur=0
    for j in range(i,len(nums)):
        cur+=nums[j]
        if cur==k:
            l+=1
print(l)
