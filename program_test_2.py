def prime(n):
    if n<=1:
        print(False)
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            print(False)
        else:
            print(True)
prime(8)




a="madam"
b=""
for i in a:
    b=i+b
    if a==b:
        print("yes")
    else:
        print("no")


a=[1,2,2,3,4,3,5]
r=[]
for i in a:
    if i not in r:
        r.append(i)
print(r)

 
    
a,b=0,1
for i in range(5):
    print(a,end=" ")
    a,b=b,a+b
