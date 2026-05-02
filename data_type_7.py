a=[9,6,4,2,3,5,7,1,0]
a.sort()
if a[0]!=0:
    print(0)
else:
    for i in a:
        if i+1 in a:
            pass
        else:
            print(i+1)
            break
let="hello"
d={}
for i in let:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
for k,v in d.items():
    if v==1:
        print(k)
        break
else:
    print(-1)


cur="A man, a plan, a canal: Panama"
add=""
for i in cur:
    if i.isalnum():
        add+=i.lower()
if add==add[::-1]:
    print(True)
else:
    print(False)


a=()
stack=[]
dic={"]":"[","}":"{",")":"("}
for i in a:
    if i in "([{":
        stack.append(i)
    elif i in ")]}":
        if not stack or stack[-1]!=dic[i]:
            print(False)
            break
        stack.pop()
    else:
        print(len(stack)==0)





a = [7,1,5,3,6,4]
mx = 0
f = a[0]

for i in a:
    if i < f:
        f = i
    pro = i - f
    if pro > mx:
        mx = pro

print(mx)
      

def prim(s):
    if s<2:
        return False
    for i in range(2,s):
        if s%i==0:
            return False
    return True
def is_prime(n):
    for i in range(2,n):
        b=n-i
        if prim(i) and prim(b):
            print(i,b)
            
is_prime(10)


a=[10,3,4,0,0,50,3]
left=0
for i in range(len(a)):
    if a[i]!=0:
        a[left]=a[i]
        left+=1
for i in range(left,len(a)):
    a[i]=0
print(a)


a=[1,2,3,1]
d={}
for i in a:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
for k,v in d.items():
    if v>1:
        print(False)
        break
else:
    print(True)




nums1 = [1,2,2,1,4]
nums2 = [2,2,4]
for i in nums1:
    for j in nums2:
        if i==j:
            print(i)
            break



