nums = [4,5,6,7,1,2]
target = 0
p=1
for i in range(len(nums)):
    if nums[i]==target:
        print(i)
        p=0
        break
if p==1:
    print(-1)


nums = [1,1,1,2,2,3]
k = 2
b={}
for i in nums:
    if i in b:
        b[i]+=1
    else:
        b[i]=1
        
for ke,v in b.items():
    if v>=k:
        print(ke)


nums = [100,4,200,1,3,2]
mx=0
l=0
for i in nums:
    if i-1 not in nums:
        cur=i
        l=1
        while cur+1 in nums:
            cur+=1
            l+=1
            mx=max(mx,l)
print(mx)



nums = [2,3,1,2,4,3]
target = 7
a=[]
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if (nums[i]+nums[j])==target:
            a.append(nums[i])
            break
print(len(a))

nums = [16,17,4,3,5,2]
for i in range(len(nums)):
    l=True
    for j in range(i+1,len(nums)):
        if nums[j]>nums[i]:
            l=False
            break
    if l:
        print(nums[i])


nums = [4,4,4]
f=float("inf")
s=float("inf")
for i in nums:
    if i>f:
        s=f
        f=i
    elif i>s and s!=f:
            s=i
if s==0:
    print("no second element")
else:
    print(s)


nums = [-2,1,-3,4,-1,2,1,-5,4]
mx=nums[0]
for i in range(len(nums)):
    t=0
    for j in range(i,len(nums)):
        t+=nums[j]
        mx=max(mx,t)
print(mx)
        

s = "hello"
vowels = "aeiou"

result = ""
for i in s:
    if i in vowels:
        result+=chr(ord(i)+1)
    else:
        result+=i
print(result)

















    
