nums = [4, 5, 2, 25]
num=[]
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i]<nums[j] and i<j:
            num.append(nums[j])
            break
if len(nums)!=len(num):
    num.append(-1)
print(num)

s = "abcabcbb"
b=0
c=[]
for i in s:
    if i not in c:
        c.append(i)
        b+=1
print(b)



nums = [2,2,1,1,1,2,2]
b={}
for i in nums:
    if i in b:
        b[i]+=1
    else:
        b[i]=1
a=len(nums)/2
for k,v in b.items():
    if v>a:
        print(k)
