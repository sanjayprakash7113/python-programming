sub="lswcpls"
mx=0
for i in range(len(sub)):
    seen=""
    n=0
    for j in range(i,len(sub)):
        if sub[j] not in seen:
            seen+=sub[j]
            n+=1
            mx=max(mx,n)
        else:
            break
print(mx)
        
s = "anagram"
t = "nagaram"
if len(s)!=len(t):
    print(False)
b={}
for i in s:
    if i in b:
        b[i]+=1
    else:
        b[i]=1
for i in t:
    if i not in b:
        print(False)
        break
    b[i]-=1
    if b[i]<0:
        print(False)
        break
else:
    print(True)


nums=[0,1,2,4]
n=0
for i in nums:
    n+=1
    if n==i:
        pass
    else:
        print(n)








    

