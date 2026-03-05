nums = [[1,3], [2,6], [8,10], [15,18]]
nums.sort()
res=[nums[0]]

for start,end in nums[1:]:
    last=res[-1][1]
    if start<=last:
        res[-1][1]=max(last,end)
    else:
        res.append([start,end])
print(res)


temps = [73,74,75,71,69,72,76,73]
temp=[]

for i in range(len(temps)):
    fount=False

    for j in range(i+1,len(temps)):
        if temps[i]<temps[j]:
            temp.append(j-i)
            fount=True
            break
    if not fount:
        temp.append(0)
print(temp)

nums = [0,3,7,2,5,8,4,6,0,1]
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



strs = ["eat","tea","tan","ate","nat","bat"]
b={}
for i in strs:
    key="".join(sorted(i))
    if key in b:
        b[key].append(i)
    else:
        b[key]=[i]
print(list(b.values()))





