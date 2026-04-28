n=3
m=10
cur=0
mul=0

for i in range(m+1):
    if i%n==0:
        mul+=i
    else:
        cur+=i
print(cur-mul)
    
a=[3,2,1,7,5,4]
odd=0
o=0

for i in range(0,len(a),2):
    if a[i]>odd:
        o=odd
        odd=a[i]
    elif a[i]>o and a[i]!=odd:
        o=a[i]
even=0
e=0
for i in range(1,len(a),2):
    if a[i]>even:
        e=even
        even=a[i]
    elif a[i]>e and a[i]!=even:
        e=a[i]
print(o+e)


le=int(input())
arr=list(int(le))
