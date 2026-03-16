nums=[2,3,4,5]
num=[]
mx=0
for i in nums:
    n=1
    for j in nums:
        if i!=j:
            n*=j
    num.append(n)
print(num)


nums=[5,4,-1,7,8]
cur=0
mx=num[0]
for i in range(len(nums)):
    cur+=nums[i]
    mx=max(mx,cur)
print(mx)


s = "leetcode"
d={}
for i in s:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
for i in range(len(s)):
    if d[s[i]] == 1:
        print(i)
        break
else:
    print(-1)

s = "{[]}"
pair={")":"(","}":"{","]":"["}
cur=[]
for i in s:
    if i in "({[":
        cur.append(i)
    else:
        if not cur:
            print(False)
            break
        if cur[-1]!=pair[i]:
            print(False)
            break
        cur.pop()
print(len(cur)==0)

list1 = [0]
list2 = []
a=list1+list2
a.sort()
print(a)






        
