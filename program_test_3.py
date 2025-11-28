a="I love python programming"
b=" "
c=1
for i in a:
    for j in b:
        if i==j:
            c=c+1
print(c)
            
a="HelloWorLD"
u=0
l=0



for i in a:
    if i.isupper():
        u=u+1
    elif i.islower():
        l=l+1
print(u)
print(l)

a=[4,3,2,6,5,1]

f=float("inf")
s=float("inf")

for n in a:
    if n<f:
        s=f
        f=n
    elif n<s and n != f:
            s=n
print(s)
        
        
a="aabbccd"
b=0
for i in a:
    for j in a:
        if i==j:
            b=b+1
if b>1:
    print(i)
    






a=[10, 21, 4, 45, 66, 93]
b=[]
for i in a:
    if i%2==0:
        b.append(i)
print(b)



a=input("")
b=input("")
for i in a:
    for j in b:
        if i==j:
            print("yes")


    
