a="hello world is welcome"
new=[]
text=""
for i in a:
 if i in a:
    text=text+i
 else:
    new.append(text)
        text=""
if text:
    new.append(text)
print(new)


a="aabbcue"
for i in a:
    count=0
    for j in a:
      if i==j:
        count=count+1
    if count==1:
        print(i)

num=[10,0,1,0]
j=0
for i in range(len(num)):
    if num[i]:#default 0
        num[i],num[j]=num[i],num[j]
        j=j+1
print(num) #output---10,1,0,0

num=[10,0,1,0]
j=len(num)-1
if i in range(len(num)-1,-1,-1):#start 4 so 4-1,end-1,-1
    if num[i]:#default 0
        num[i],num[j]=num[j],num[i]
        j=j-1
print(num) #output--0,0,10,0

num=[1,2,3,4,5,6]
target=8
ans=[]
for i in range(len(num)):
 for j in range(i+1,len(num)):
    if num[i]+num[j]==target:
        ans.append((num[i],num[j])) 
print(ans)