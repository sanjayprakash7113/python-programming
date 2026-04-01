

s="madam"
left=0
right=len(s)-1

pal=True

while left<right:
    if s[left]!=s[right]:
        pal=False
        break
    left+=1
    right-=1
print(pal)


s="A man, a plan, a canal: Panama"
cur=""
for i in s:
    if i.isalnum():
        cur+=i.lower()
left=0
right=len(cur)-1

pal=True

while left<right:
    if cur[left]!=cur[right]:
        pal=False
        break
    left+=1
    right-=1
print(pal)


nums = [1,2,3,2,4]
target = 4
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i]+nums[j]==target:
            print((nums[i],nums[j]))



dub=set()
res=set()

for i in nums:
    need=target-i
    if need in dub:
        pair=tuple(sorted((need,i)))
        res.add(pair)
    dub.add(i)
print(list(res))





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

height = [1,8,6,2,5,4,8,3,7]
mx=0
for i in range(len(height)):
    for j in range(i+1,len(height)):
        pair=(min(height[i],height[j]))*(j-i)
        mx=max(mx,pair)
print(mx)



nums = [1,1,1]
k = 2
l=0
for i in range(len(nums)):
    cur=0
    for j in range(1,len(nums)):
        cur+=nums[j]
        if cur==k:
            l+=1
        else:
            break  
print(l)
              



par="({[})"

dic={"}":"{","]":"[",")":"("}
stack=[]

for i in par:
    if i in dic:
        if not stack or stack[-1]!=dic[i]:
            print(False)
            break
        stack.pop()
    else:
        stack.append(i)
print(len(stack)==0)
        


















        
    
