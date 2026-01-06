n=5
for i in range(n+1):
    for j in range(i):
            print(" ",end=" ")
    for s in range(n-i):
            print("*",end=" ")
    print()

n=4
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for s in range(1,i+1):
            print(s,end=" ")
    print()

n=4
for i in range(n):
    for j in range(i):
        print(" ",end=" ")
    for s in range(i+1,n+1):
        print(s,end=" ")
    print()
n=4
for i in range(n+1):
    for j in range(i):
        print("*",end=" ")
    print()

n=4
for i in range(n+1):
    for j in range(n-i):
        print("*",end=" ")
    for s in range(i):
        print(" ",end=" ")
    print()


a=5
for i in range(1,a+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
for i in range(a-1,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()


n=5
for i in range(n+1):
    for j in range(i):
        print(" ",end=" ")
    for s in range(i+1,n+1):
        print(s,end=" ")
    print()
