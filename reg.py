n=5
def s(n):
    if n==1:
        return 1
    else:
        return n+s(n-1)
print(s(n))

def v1(n):
    if n==0:
        return 0
    else:
        return (n%10)+v1(n//10)
print(v1(100))

l1=[8,5,4,8,1,2,1,2,8,5,8,7,9]
l2=[8,1,2]








     
   