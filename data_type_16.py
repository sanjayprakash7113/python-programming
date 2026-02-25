height = [1,8,6,2,5,4,8,3,7]
a=0
for i in range(len(height)):
    for j in range(i+1,len(height)):
        res=height[j]-height[i]
        if res>a:
            a=res
print(a*a)


n=4
for i in range(1,n):
    for j in range(i):
        print("*",end= " ")
    print()

n=6
for i in range(1,n):
    for j in range(i,n-1):
        print("*",end=" ")
    print()

n=7
for i in range(n):
    for j in range(1,i+1):
        print(i,end=" ")
    print()

n = 5
for i in range(1, n+1):
    print(" " * (n - i),end="")   # spaces
    for j in range(i):
        print("* ",end="")
    print()








