nums = [5,4,3]
gr=[]
for i in range(len(nums)):
    add=-1
    for j in range(i+1,len(nums)):
        if nums[j]>nums[i]:
            add=nums[j]
    gr.append(add)
print(gr)


nums = [2,2,1,1,1,2,2]
half=len(nums)//2
b={}
for i in nums:
    if i in b:
        b[i]+=1
    else:
        b[i]=1
o=0
for k,v in b.items():
    if v>half:
        o=k
print(o)
        
    
nums = [3,0,1]
n=0
while True:
    if n not in nums:
        print(n)
        break
    else:
        n+=1


nums = [100,4,200,1,3,2]
ma_x=0
l=0
for i in nums:
    if i-1 not in nums:
        v=i
        l=1
        while v+1 in nums:
            v+=1
            l+=1
            ma_x=max(ma_x,l)
print(ma_x)


nums = [4,3,2,7,8,2,3,1]
dub=set()
for i in nums:
    if i in dub:
        print(i,end=" ")
    else:
        dub.add(i)
















        
