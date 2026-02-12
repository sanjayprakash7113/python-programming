nums=[4,0,1]
nums.sort()
i=0
for j in nums:
    if i==j:
        i+=1
    else:
        print(i)
        break


        
    

st=[7,1,5,3,6,4]
cur=st[0]
max_l=0
for i in range(len(st)):
    while st[i]<cur:
        cur=st[i]
    max_l=max(max_l,st[i]-cur)
print(max_l)


b=[]
for i in range(len(st)):
    for j in range(i+1,len(st)):
        if st[i]<st[j]:
            b.append(st[j]-st[i])
print(max(b))
