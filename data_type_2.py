n=input()
num=""
for i in n:
    if i=="0":
        num+="1"
    else:
        num+=i
print(num)

n=input()
for i in n:
    if i=="0":
        print("1",end="")
    else:
        print(i,end="")

def count(s):
    if not s or s[0]=="0":
        return 0
    n=len(s)
    dp=[0]*(n+1)
    dp[0]=1
    dp[1]=1
    for i in range(2,n+1):
        if s[i-1]!="0":
            dp[i]+=dp[i-1]
        two=int(s[i-2:i])
        if 10<=two<=26:
            dp[i]+=dp[i-2]
    print(dp[n])
count("226")


def prim(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
def is_prim(s):
    for a in range(2,s):
        b=s-a
        if prim(a) and prim(b):
            print(a,b)
            return
n=int(input())
is_prim(n)
    
n=input()
for i in n:
    if i=="0":
        print("1",end="")
    else:
        print(i,end="")
