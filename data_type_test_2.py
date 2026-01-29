s = "swiss"
b={}
for i in s:
    if i in b:
        b[i]+=1
    else:
        b[i]=1
for k,v in b.items():
    if v==1:
        print(k)
        break


s = "Python is very powerful language"
l=0
a=s.split()
ans=""
for i in a:
    if len(i)>l:
        l=len(i)
        ans=i
print(ans)


s = "apple banana apple orange banana apple"
s=s.split()
b={}
for i in s:
    if i in b:
        b[i]+=1
    else:
        b[i]=1
c=0
ans=""
for k,v in b.items():
    if v>c:
        c=v
        ans=k
print(ans)



nums = [3, 5, 1, 4, 5, 3]
b={}
ans=0
for i in nums:
    if i in b:
        ans=i
        break
    else:
        b[i]=1
print(ans)

