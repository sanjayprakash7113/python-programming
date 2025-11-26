a="python"
b=""
for i in a:
    b=i+b
    print(b)

        
a=234
b=str(a)
c=0
for i in b:
    c=c+int(i)
    print(c)


a="hello world"
b="aeiou"
c=0
for i in a:
    for j in b:
        if i==j:
            c=c+1
            print(c)



a=[10,23,21]
print(max(a))

def ams(n):
    s=str(n)
    e=len(s)
    tot=sum(int(d)**e for d in s)
    if tot==n:
        print(n)
    else:
        print("non")
ams(123)


for i in range(1,6):
    for j in range(i):
        print("*",end=" ")
    print()
   
    
